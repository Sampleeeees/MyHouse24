import datetime
from django.utils import timezone
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.forms import modelformset_factory, formset_factory
from django.views.generic import UpdateView, DeleteView, TemplateView, View, ListView, CreateView, DetailView
from .models import Measure, Service, Tarrif, ServiceforTariif
from .forms import ServiceForm, MeasureForm, TarrifForm, ServiceforTariifForm, UserForm
from Articles_and_detail_payments.models import PaymentDetail, Article
from Articles_and_detail_payments.forms import PaymentForm, ArticleForm
from User.models import User, Role
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
UserModel = get_user_model()
from django.db.models import Q

class SettingServiceUpdate(View):
    def get(self, request, *args, **kwargs):
        ServiceFormset = modelformset_factory(Service, form=ServiceForm, extra=0, can_delete=True)
        MeasureFormset = modelformset_factory(Measure, form=MeasureForm, extra=0, can_delete=True)
        service_formset = ServiceFormset(queryset=Service.objects.all(), prefix='form-service')
        measure_formset = MeasureFormset(queryset=Measure.objects.all(), prefix='measure')


        context = {
            'service_formset': service_formset,
            'measure_formset': measure_formset,
            'all_measure': Measure.objects.all(),
        }
        return render(request, 'Tarrif_and_services/servicesAndMeasureEdit.html', context)

    def post(self, request, *args, **kwargs):
        MeasureFormset = modelformset_factory(Measure, form=MeasureForm, extra=0, can_delete=True)
        measure_formset = MeasureFormset(self.request.POST, queryset=Measure.objects.all(), prefix='measure')
        ServiceFormset = modelformset_factory(Service, form=ServiceForm, extra=0, can_delete=True)
        service_formset = ServiceFormset(self.request.POST, queryset=Service.objects.all(), prefix='form-service')

        if self.request.POST:
            if measure_formset.is_valid() and service_formset.is_valid():
                for measure in measure_formset:
                    measure.save()
                measure_formset.save()
                for service in service_formset:
                    print(self.request.POST.get(f'{service.prefix}-measure'))
                    serv = service.save(commit=False)
                    serv.measure_id = Measure.objects.get(pk=self.request.POST.get(f'{service.prefix}-measure')).id
                    serv.save()
                service_formset.save()

        context = {
            'measure_formset': measure_formset,
            'service_formset': service_formset,
            'all_measure': Measure.objects.all(),
        }
        return render(request, 'Tarrif_and_services/servicesAndMeasureEdit.html', context)



class PaymentUpdate(UpdateView):
    model = PaymentDetail
    template_name = 'Tarrif_and_services/PaymentUpdate.html'
    form_class = PaymentForm
    success_url = reverse_lazy('paymentUpdate')

    def get_object(self, queryset=None):
        return PaymentDetail.objects.first()

    def get_context_data(self, **kwargs):
        context = super(PaymentUpdate, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        form.save()
        return super().form_valid(form=form)

class TarrifList(ListView):
    model = Tarrif
    template_name = 'Tarrif_and_services/tarrifList.html'
    queryset = Tarrif.objects.all()

class TarrifCreate(CreateView):
    model = Tarrif
    template_name = 'Tarrif_and_services/tarrifCreate.html'
    form_class = TarrifForm
    success_url = reverse_lazy('tarrifList')

    def get_context_data(self, **kwargs):
        context =super(TarrifCreate, self).get_context_data(**kwargs)
        print(context)
        ServiceForTarrifFormset = modelformset_factory(ServiceforTariif, form=ServiceforTariifForm, extra=0, can_delete=True)
        if self.request.POST:
            context['formset_service_price'] = ServiceForTarrifFormset(self.request.POST, prefix='service-amount', queryset=ServiceforTariif.objects.none())
        else:
            context['formset_service_price'] = ServiceForTarrifFormset(prefix='service-amount', queryset=ServiceforTariif.objects.none())
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        terrif = form.save(commit=False)
        terrif.published = timezone.now()
        terrif.save()
        print(terrif)
        if context['formset_service_price'].is_valid:
            for service_price in context['formset_service_price']:
                price = service_price.save(commit=False)
                price.tarrif_id = terrif.id
                price.save()
            context['formset_service_price'].save()
        return super().form_valid(form=form)


class TarrifCopyView(CreateView):
    model = Tarrif
    form_class = TarrifForm
    template_name = 'Tarrif_and_services/tarrifCopy.html'
    success_url = reverse_lazy('tarrifList')

    def get_initial(self):
        # Отримання початкових значень для форми копіювання тарифу
        tarrif = Tarrif.objects.get(pk=self.kwargs['pk'])
        initial = {
            'name_tarrif': tarrif.name_tarrif,  # Замініть field1 на реальні поля моделі Tarrif, які потрібно скопіювати
            'description_tarrif': tarrif.description_tarrif,
            # Додайте інші поля моделі, які потрібно скопіювати
        }
        return initial

    def get_context_data(self, **kwargs):
        context = super(TarrifCopyView, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        ServiceForTarrifFormset = modelformset_factory(
            ServiceforTariif, form=ServiceforTariifForm, extra=0, can_delete=True
        )
        if self.request.POST:
            context['formset_service_price'] = ServiceForTarrifFormset(
                self.request.POST, prefix='service-amount', queryset=ServiceforTariif.objects.none()
            )
        else:
            tarrif = Tarrif.objects.get(pk=self.kwargs['pk'])
            context['formset_service_price'] = ServiceForTarrifFormset(
                prefix='service-amount', queryset=ServiceforTariif.objects.filter(tarrif_id=tarrif.id)
            )
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        tarrif = form.save(commit=False)
        tarrif.published = timezone.now()
        tarrif.save()
        if context['formset_service_price'].is_valid():
            for service in context['formset_service_price']:
                servi = service.save(commit=False)
                servi.tarrif_id = tarrif.id
                servi.save()
            context['formset_service_price'].save()
        return super().form_valid(form)


class TarrifUpdate(UpdateView):
    model = Tarrif
    template_name = 'Tarrif_and_services/tarrifUpdate.html'
    form_class = TarrifForm
    success_url = reverse_lazy('tarrifList')


    def get_context_data(self, **kwargs):
        context = super(TarrifUpdate, self).get_context_data(**kwargs)
        ServiceForTarrifFormset = modelformset_factory(ServiceforTariif, form=ServiceforTariifForm, extra=0, can_delete=True)
        if self.request.POST:
            context['formset_service_price'] = ServiceForTarrifFormset(self.request.POST, prefix='service-amount', queryset=ServiceforTariif.objects.filter(tarrif_id=context['tarrif'].id))
        else:
            context['formset_service_price'] = ServiceForTarrifFormset(prefix='service-amount', queryset=ServiceforTariif.objects.filter(tarrif_id=context['tarrif'].id))
        return context

    def form_valid(self, form):
        context =self.get_context_data(form=form)
        tarrif = form.save(commit=False)
        tarrif.published = timezone.now()
        tarrif.save()
        if context['formset_service_price'].is_valid():
            for service in context['formset_service_price']:
                servi = service.save(commit=False)
                servi.tarrif_id = tarrif.id
                servi.save()
            context['formset_service_price'].save()
        return super().form_valid(form)


class TarrifDetail(DeleteView):
    model = Tarrif
    template_name = 'Tarrif_and_services/tarrifDetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ServiceForTarrifFormset = modelformset_factory(ServiceforTariif, form=ServiceforTariifForm, extra=0, can_delete=True)
        context['formset_service_price'] = ServiceForTarrifFormset(prefix='service-amount', queryset=ServiceforTariif.objects.filter(tarrif_id=context['object'].id))
        context['service_list'] = ServiceforTariif.objects.filter(tarrif_id=context['object'].id)
        return context




class ArticleList(ListView):
    model = Article
    template_name = 'Tarrif_and_services/articleList.html'
    queryset = Article.objects.all()


class ArticleCreate(CreateView):
    model = Article
    template_name = 'Tarrif_and_services/articleCreate.html'
    form_class = ArticleForm
    success_url = reverse_lazy('articleList')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ArticleUpdate(UpdateView):
    model = Article
    template_name = 'Tarrif_and_services/articleUpdate.html'
    form_class = ArticleForm
    success_url = reverse_lazy('articleList')



class UsersList(ListView):
    model = User
    template_name = 'Tarrif_and_services/usersList.html'
    queryset = User.objects.all()


class UserDetail(DetailView):
    model = User
    template_name = 'Tarrif_and_services/user_detail.html'


class UserCreate(CreateView):
    model = User
    template_name = 'Tarrif_and_services/user_create.html'
    form_class = UserForm
    success_url = reverse_lazy('usersList')

    def get_context_data(self, **kwargs):
        context = super(UserCreate, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        print(form.errors)
        if form.is_valid():
            form.save()
            login(self.request, self.request.user, backend='User.backends.EmailBackend')
        else:
            print(form.errors)
        return super().form_valid(form=form)

class UserUpdate(UpdateView):
    model = User
    template_name = 'Tarrif_and_services/usersEdit.html'
    form_class = UserForm
    success_url = reverse_lazy('usersList')

    def get_context_data(self, **kwargs):
        context = super(UserUpdate, self).get_context_data(**kwargs)
        print(context['object'].id)
        print(self.request.user)
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        print(form.cleaned_data)
        if form.cleaned_data.get('password1') == form.cleaned_data.get('password2') and form.cleaned_data.get('password1') != '':
            print('We here!')
            user = User.objects.get(pk=context['object'].id)
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
            login(self.request, self.request.user, backend='User.backends.EmailBackend')
        else:
            print('else')
            form.save()
        return super().form_valid(form=form)



class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('usersList')

    def get(self, request, *args, **kwargs):
        return self.delete(self, request, *args, **kwargs)

class UserSend(View):
    def get(self, request, user_id, *args, **kwargs):
        print('Hello')
        print(self.request)
        if self.request:
            print(user_id)
            user = User.objects.get(pk=user_id)
            current_site = get_current_site(self.request)
            mail_subject = 'Вас запросили до MyHouse24.'
            message = render_to_string('Tarrif_and_services/send_invite_to_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = user.email
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            print('Sending')
            return redirect('usersList')
        else:
            print(self.request.user.id)
            print(user_id)
            return HttpResponse('Not working')


class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('articleList')

    def get(self, request, *args, **kwargs):
        return self.delete(self, request, *args, **kwargs)




class MeasureDelete(DeleteView):
    model = Measure
    success_url = reverse_lazy('setting_service')

    def get(self, request, *args, **kwargs):
        return self.delete(self, request, *args, **kwargs)

class ServiceDelete(DeleteView):
    model = Service
    success_url = reverse_lazy('setting_service')

    def get(self, request, *args, **kwargs):
        return self.delete(self, request, *args, **kwargs)

class TarrifDelete(DeleteView):
    model = Tarrif
    success_url = reverse_lazy('tarrifList')

    def get(self, request, *args, **kwargs):
        return self.delete(self, request, *args, **kwargs)


def check_measure(request):
    print(request.GET.get('service_id'))
    if request.GET.get('service_id') != '' and request.GET.get('service_id') is not None:
        print('Works')
        measure = serializers.serialize('json', Service.objects.filter(pk=request.GET.get('service_id')))
        all_measure = serializers.serialize('json', Measure.objects.all())
        return JsonResponse({'measure': measure, 'all_measure': all_measure}, status=200)
    else:
        print('Zero to hero')
        return JsonResponse({'measure': 0, 'all_measure': 0}, status=200)
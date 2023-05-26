import json
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DeleteView, DetailView, UpdateView, CreateView
from Tarrif_and_services.models import ServiceforTariif
from Master_application.models import MatsterApplication
from Personal_book.models import PersonalBook
from Receipt.models import Receipt
from Front_pages.models import *
from .models import *
from .forms import AppartamentForm
from Tarrif_and_services.forms import UserForm
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.db.models import Q
from Statement.models import Statement
from User.models import User

UserModel = get_user_model()


# Create your views here.

class BaseView(View):
    def get(self, request):
        general = GeneralPage.objects.first()
        contact = Contacts.objects.first()

        users = User.objects.all()
        print('USERS:', users)
        context = {
            'users': users,
            'user_count': User.objects.all().count()
        }


        return render(request, 'Appartament/base.html', context=context)


class AppartamentList(ListView):
    model = Appartament
    template_name = 'Appartament/appartament_list.html'
    queryset = Appartament.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AppartamentList, self).get_context_data(**kwargs)
        context['houses'] = House.objects.all()
        context['owners'] = User.objects.filter(appartament__isnull=False).distinct()
        return context


class AppartamentDetail(DetailView):
    model = Appartament
    template_name = 'Appartament/appartament_detail.html'


class AppartamentCreate(CreateView):
    template_name = 'Appartament/appartament_create.html'
    form_class = AppartamentForm
    success_url = reverse_lazy('appartament_list')

    def form_valid(self, form):
        if self.request.POST.get('action_save'):
            form.save()
            return redirect('appartament_list')
        elif self.request.POST.get('action_save_add'):
            form.save()
            return redirect('appartament_create')
        return super().form_valid(form=form)

class AppartamentUpdate(UpdateView):
    model = Appartament
    template_name = 'Appartament/appartament_update.html'
    form_class = AppartamentForm
    success_url = reverse_lazy('appartament_list')

    def get_context_data(self, **kwargs):
        context = super(AppartamentUpdate, self).get_context_data(**kwargs)
        context['personals'] = Appartament.objects.filter(personalbook__PersonalBook__ownerAppartemnt_id__isnull=False)
        return context
    def form_valid(self, form):
        if self.request.POST.get('action_save'):
            form.save()
            return redirect('appartament_list')
        elif self.request.POST.get('action_save_add'):
            form.save()
            return redirect('appartament_create')
        return super().form_valid(form=form)


class AppartamentDelete(DeleteView):
    model = Appartament
    success_url = reverse_lazy('appartament_list')

    def get(self, request, *args, **kwargs):
        return self.delete(self, request, *args, **kwargs)


# Власники квартир
class OwnerAppartamentsList(ListView):
    model = User
    template_name = 'Appartament/owner_appartaments_list.html'
    queryset = User.objects.filter(appartament__isnull=False).distinct()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OwnerAppartamentsList, self).get_context_data(**kwargs)
        context['appartament'] = Appartament.objects.all()
        context['house'] = House.objects.all()
        context['count_owner'] = User.objects.filter(appartament__isnull=False).distinct().count()
        return context


# Додати власника квартири
class AddOwnerAppartamentCreate(CreateView):
    form_class = UserForm
    template_name = 'Appartament/add_owner_appartament_create.html'
    success_url = reverse_lazy('ownerAppartamentsList')

    def form_valid(self, form):
        print(form.errors)
        if form.is_valid():
            form.save()
            login(self.request, self.request.user, backend='User.backends.EmailBackend')
        else:
            print(form.errors)
        return super().form_valid(form=form)


class SendInviteOwnerAppartament(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Appartament/send_page.html')

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('email') != '':
            user = User.objects.get(email=self.request.POST.get('email'))
            current_site = get_current_site(self.request)
            mail_subject = 'Вас запросили до MyHouse24.'
            message = render_to_string('Appartament/send_invite_email.html', {
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
            return redirect('ownerAppartamentsList')
        else:
            return HttpResponse('Sendnot working')


class SendEmailInviteOwnerAppartament(View):
    pass


# Редагування власників квартир
class OwnerAppartamentUpdate(UpdateView):
    model = User
    template_name = 'Appartament/owner_appartament_update.html'
    form_class = UserForm
    success_url = reverse_lazy('ownerAppartamentsList')

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        print(form.cleaned_data)
        if form.cleaned_data.get('password1') == form.cleaned_data.get('password2') and form.cleaned_data.get(
                'password1') != '':
            print('We here!')
            user = User.objects.get(pk=context['object'].id)
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
            login(self.request, self.request.user, backend='User.backends.EmailBackend')
        else:
            print('else')
            form.save()
        return super().form_valid(form=form)


# Видалення Власника квартир
class OwnerAppartamentDelete(DeleteView):
    model = User
    success_url = reverse_lazy('ownerAppartamentsList')

    def get(self, request, *args, **kwargs):
        return self.delete(self, request, *args, **kwargs)


# Filters


# Фільтер для залежності між будинком та секціями з поверхом
def filter_house(request):
    print(request.GET.get('house_id'))
    if request.GET.get('house_id') != '' and request.GET.get('house_id') is not None:
        print('Hello')
        sections = serialize('json', Section.objects.filter(house_id=request.GET.get('house_id')))
        floors = serialize('json', Floor.objects.filter(house_id=request.GET.get('house_id')))
        all_appartament = serialize('json', Appartament.objects.filter(house_id=request.GET.get('house_id')))
        return JsonResponse({'sections': sections, 'floors': floors, 'all_appartament': all_appartament}, status=200)
    else:
        print('Not Working')
        return JsonResponse({}, status=200)


def owner_appartament_list(request):
    owners = User.objects.filter(appartament__isnull=False).distinct('id')

    # Пошук даних
    search_owner_id = request.GET.get('owner_id')
    search_owner_fio = request.GET.get('owner_fio')
    search_owner_phone = request.GET.get('owner_phone')
    search_owner_email = request.GET.get('owner_email')
    search_owner_house = request.GET.get('owner_house')
    search_owner_flat = request.GET.get('owner_flat')
    search_owner_status = request.GET.get('owner_status')

    print(search_owner_status)

    query = Q()

    if search_owner_id:
        query &= Q(id__icontains=search_owner_id, appartament__isnull=False)

    if search_owner_fio:
        query &= Q(first_name__icontains=search_owner_fio, appartament__isnull=False)

    if search_owner_phone:
        query &= Q(phone_number__icontains=search_owner_phone, appartament__isnull=False)

    if search_owner_email:
        query &= Q(email__icontains=search_owner_email, appartament__isnull=False)

    if search_owner_house:
        query &= Q(appartament__house_id=search_owner_house, appartament__isnull=False)

    if search_owner_flat:
        query &= Q(appartament__isnull=False, appartament__number_appartament__icontains=search_owner_flat)

    if search_owner_status:
        query &= Q(status__icontains=search_owner_status, appartament__isnull=False)

    owners = owners.filter(query).distinct()

    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))

    paginator = Paginator(owners, length)
    owners = paginator.get_page(start // length + 1)

    data = []

    for owner in owners:
        data.append({
            'id': owner.id,
            'fio': owner.get_full_name(),
            'phone': owner.phone_number,
            'email': owner.email,
            'house': serialize('json', House.objects.filter(appartament__owner_id=owner.id)),
            'flat': serialize('json', Appartament.objects.filter(owner_id=owner.id)),
            'date': '',
            'status': owner.get_status_display(),
            'borg': ''
        })

    response = {
        'draw': request.GET.get('draw'),
        'recordsTotal': User.objects.filter(appartament__isnull=False).distinct('id').count(),
        'recordsFiltered': owners.paginator.count,
        'data': data
    }

    return JsonResponse(response)


def appartament_list(request):
    flats = Appartament.objects.all()

    search_flat_number = request.GET.get('flat_number')
    search_flat_home = request.GET.get('flat_home')
    search_flat_section = request.GET.get('flat_section')
    search_flat_floor = request.GET.get('flat_floor')
    search_flat_owner = request.GET.get('flat_owner')
    search_flat_residual = request.GET.get('flat_residual')

    print(search_flat_number)

    query = Q()

    if search_flat_number:
        query &= Q(number_appartament__icontains=search_flat_number)

    if search_flat_home:
        query &= Q(house_id=search_flat_home)

    if search_flat_section:
        query &= Q(section_id=search_flat_section)

    if search_flat_floor:
        query &= Q(floor_id=search_flat_floor)

    if search_flat_owner:
        query &= Q(owner_id=search_flat_owner)

    flats = flats.filter(query)

    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))

    paginator = Paginator(flats, length)
    flats = paginator.get_page(start // length + 1)

    data = []

    for flat in flats:
        try:
            statement = Statement.objects.filter(ownerAppartemnt=flat.owner.id,
                                                 personal_book__appartament_id=flat.id).first()
            data.append({
                'id': flat.id,
                'number': flat.number_appartament,
                'home': flat.house.name_home,
                'section': flat.section.name_section,
                'floor': flat.floor.name_floor,
                'owner': flat.owner.get_full_name(),
                'residual': statement.amount if statement else ''
            })
        except Statement.DoesNotExist:
            data.append({
                'id': flat.id,
                'number': flat.number_appartament,
                'home': flat.house.name_home,
                'section': flat.section.name_section,
                'floor': flat.floor.name_floor,
                'owner': flat.owner.get_full_name(),
                'residual': ''
            })

    response = {
        'draw': request.GET.get('draw'),
        'recordsTotal': Appartament.objects.all().count(),
        'recordsFiltered': flats.paginator.count,
        'data': data
    }

    return JsonResponse(response)


def Statistic(request):
    statements = Statement.objects.all()

    # Створення словника для передачі у контекст
    data = {}
    income = 0
    expense = 0
    for statement in statements:
        month = statement.date_published.strftime('%B')  # Отримання назви місяця
        if statement.amount > 0:
            income += statement.amount
        else:
            expense += -statement.amount
        data[month] = {
            'income': income,
            'expense': expense
        }

    plus = Statement.objects.filter(amount__gt=0)
    total_plus = 0
    for stat_plus in plus:
        total_plus += stat_plus.amount

    minus = Statement.objects.filter(amount__lt=0)
    total_minus = 0
    for stat_minus in minus:
        total_minus -= stat_minus.amount

    receipts = Receipt.objects.all()
    total_receipt = 0
    for receipt in receipts:
        services = ServiceforTariif.objects.filter(tarrif_id=receipt.tarrif.id)
        for cina in services:
            total_receipt += cina.price * cina.consum

    flat_total = 0
    for flat in Appartament.objects.all():
        try:
            stat = Statement.objects.get(ownerAppartemnt=flat.owner.id, personal_book__appartament_id=flat.id)
            flat_total += stat.amount
        except Statement.DoesNotExist:
            flat_total += 0


    context = {
        'house_count': House.objects.all().count(),
        'active_owners': User.objects.filter(appartament__isnull=False, status='1000').count(),
        'masters_application': MatsterApplication.objects.filter(status='В роботі').count(),\
        'flats': Appartament.objects.all().count(),
        'personals': PersonalBook.objects.all().count(),
        'masters': MatsterApplication.objects.all().count(),
        'data': json.dumps(data),
        'total': total_plus - total_minus,
        'total_receipt': total_receipt,
        'flat_total': flat_total
    }
    return render(request, 'Appartament/general.html', context=context)





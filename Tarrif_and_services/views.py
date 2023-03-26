from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.forms import modelformset_factory, formset_factory
from django.views.generic import UpdateView, DeleteView, TemplateView, View, ListView, CreateView
from .models import Measure, Service, Tarrif, ServiceforTariif
from .forms import ServiceForm, MeasureForm, TarrifForm, ServiceforTariifForm
from Articles_and_detail_payments.models import PaymentDetail, Article
from Articles_and_detail_payments.forms import PaymentForm, ArticleForm
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
        context['object'].save()
        return super().form_valid(form=form)

class TarrifList(ListView):
    model = Tarrif
    template_name = 'Tarrif_and_services/tarrifList.html'
    queryset = Tarrif.objects.all()

class TarrifCreate(CreateView):
    model = Tarrif
    template_name = 'Tarrif_and_services/tarrifCreate.html'
    form_class = TarrifForm

    def get_context_data(self, **kwargs):
        context =super(TarrifCreate, self).get_context_data(**kwargs)
        ServiceForTarrifFormset = modelformset_factory(ServiceforTariif, form=ServiceforTariifForm, extra=0, can_delete=True)
        if self.request.POST:
            context['formset_service_price'] = ServiceForTarrifFormset(self.request.POST, prefix='service-amount', queryset=ServiceforTariif.objects.none())
        else:
            context['formset_service_price'] = ServiceForTarrifFormset(prefix='service-amount', queryset=ServiceforTariif.objects.none())
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        return super().form_valid(form)



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

def check_measure(request):
    print(request.GET.get('service_id'))
    if request.GET.get('service_id') != '' and request.GET.get('service_id') is not None:
        print('Works')
        measure = serializers.serialize('json', Service.objects.filter(pk=request.GET.get('service_id')))
        all_measure = serializers.serialize('json', Measure.objects.all())
        return JsonResponse({'measure': measure, 'all_measure': all_measure}, status=200)
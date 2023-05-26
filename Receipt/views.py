import json
import random
from Statement.models import Statement
from django.core import serializers
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.forms import modelformset_factory
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from django.db.models import Q
from Tarrif_and_services.models import Measure, Service
import Meters_data.models
import Personal_book.models
from .models import Receipt
from User.models import User
from .forms import ReceiptForm
from House.models import House, Section
from Appartament.models import Appartament
from Tarrif_and_services.models import ServiceforTariif, Tarrif
from Tarrif_and_services.forms import ServiceforTariifForm
from datetime import datetime
from dateutil import tz, relativedelta
from Meters_data.models import MetersData

# Встановлення української локалізації
ukrainian_locale = tz.gettz('Europe/Kiev')

# Встановлення українських назв місяців
ukrainian_month_names = [
    'Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень',
    'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень'
]

# Отримання поточної дати та часу з українською локалізацією
now = datetime.now(ukrainian_locale)

# Отримання української назви місяця
ukrainian_month_name = ukrainian_month_names[now.month - 1]


class ReceiptList(ListView):
    model = Receipt
    template_name = 'Receipt/receipt_list.html'
    queryset = Receipt.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ReceiptList, self).get_context_data(**kwargs)
        context['owners'] = User.objects.filter(appartament__isnull=False).distinct()
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

        context['flat_total'] = flat_total
        context['total_plus'] = total_plus
        context['total_minus'] = -total_minus
        context['total'] = total_plus - total_minus
        context['total_receipt'] = total_receipt

        return context



class ReceiptCreate(CreateView):
    model = Receipt
    template_name = 'Receipt/receipt_create.html'
    form_class = ReceiptForm
    success_url = reverse_lazy('ReceiptList')

    def get_context_data(self, **kwargs):
        context = super(ReceiptCreate, self).get_context_data(**kwargs)
        context['measures'] = Measure.objects.all()
        ServiceForTarrifFormset = modelformset_factory(ServiceforTariif, form=ServiceforTariifForm, extra=0, can_delete=True)
        if self.request.POST:
            context['formset_receipt_service'] = ServiceForTarrifFormset(self.request.POST, prefix='receipt-service', queryset=ServiceforTariif.objects.none())
        else:
            context['formset_receipt_service'] = ServiceForTarrifFormset(prefix='receipt-service', queryset=ServiceforTariif.objects.none())
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        new_tariff = Tarrif.objects.create(name_tarrif=str('Tarrif№'+form.cleaned_data['uid']), published=datetime.now())
        form_update = form.save(commit=False)
        form_update.tarrif = new_tariff
        form.save()

        suma = 0


        print(context['formset_receipt_service'])
        print('FORM', form.cleaned_data['tarrif'])
        for formset in context['formset_receipt_service']:
            receipt_formset = formset.save(commit=False)
            receipt_formset.tarrif_id = new_tariff.id
            receipt_formset.save()

        context['formset_receipt_service'].save()

        return super().form_valid(form=form)

class ReceiptUpdate(UpdateView):
    model = Receipt
    template_name = 'Receipt/receipt_update.html'
    form_class = ReceiptForm
    success_url = reverse_lazy('ReceiptList')

    def get_context_data(self, **kwargs):
        context = super(ReceiptUpdate, self).get_context_data(**kwargs)
        context['measures'] = Measure.objects.all()
        ServiceForTarrifFormset = modelformset_factory(ServiceforTariif, form=ServiceforTariifForm, extra=0, can_delete=True)
        if self.request.POST:
            context['formset_receipt_service'] = ServiceForTarrifFormset(self.request.POST, prefix='receipt-service', queryset=ServiceforTariif.objects.filter(tarrif_id=context['object'].tarrif.id))
        else:
            context['formset_receipt_service'] = ServiceForTarrifFormset(prefix='receipt-service', queryset=ServiceforTariif.objects.filter(tarrif_id=context['object'].tarrif.id))
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        context['formset_receipt_service'].save()

        return super().form_valid(form=form)

class ReceiptDelete(DeleteView):
    model = Receipt
    success_url = reverse_lazy('ReceiptList')

    def get(self, request, *args, **kwargs):
        return self.delete(self, request, *args, **kwargs)

def filter_house_receipt(request):
    if request.GET.get('house_id') != '' and request.GET.get('house_id') is not None:
        print('Hello')
        sectionss = Section.objects.filter(house_id=request.GET.get('house_id'))
        sec = []
        for section in sectionss:
            section.name_home = section.house.name_home
            sec.append(section)

        sections = serialize('json', sec)
        return JsonResponse({'sections': sections}, status=200)
    else:
        print('Not Working')
        return JsonResponse({}, status=200)

def filter_appartament_receipt(request):
    if request.GET.get('house_id') != '' and request.GET.get('section_id') != '':
        appartaments = serialize('json', Appartament.objects.filter(house_id=request.GET.get('house_id'), section_id=request.GET.get('section_id')), use_natural_foreign_keys=True)
        return JsonResponse({'appartaments': appartaments}, status=200)
    else:
        return JsonResponse({}, status=200)


def appartament_detail_receipt(request):
    if request.GET.get('flat_id') != '' and request.GET.get('flat_id') is not None:
        owner_name = serialize('json', User.objects.filter(appartament__id=request.GET.get('flat_id')))
        personal = serialize('json', Personal_book.models.PersonalBook.objects.filter(appartament_id=request.GET.get('flat_id')))
        meters = serialize('json', Meters_data.models.MetersData.objects.filter(appartament_id=request.GET.get('flat_id')), use_natural_foreign_keys=True)
        return JsonResponse({'owner': owner_name, 'personal': personal, 'meters': meters}, status=200)
    else:
        return JsonResponse({}, status=200)


def receipt_list(request):
    receipts = Receipt.objects.all()



    #SEARCH
    search_num_receipt = request.GET.get('num_receipt')
    search_status_receipt = request.GET.get('status_receipt')
    search_date_receipt = request.GET.get('date_receipt')
    search_month_receipt = request.GET.get('month_receipt')
    search_flat_receipt = request.GET.get('flat_receipt')
    search_owner_receipt = request.GET.get('owner_receipt')
    search_confirm_receipt = request.GET.get('confirm_receipt')

    query = Q()

    if search_num_receipt:
        query &= Q(uid__icontains=search_num_receipt)

    if search_status_receipt:
        query &= Q(status_pay=search_status_receipt)

    if search_date_receipt:
        start = datetime.strptime(search_date_receipt[0:10], '%d.%m.%Y').date()
        end = datetime.strptime(search_date_receipt[13:23], '%d.%m.%Y').date()
        print()
        print('date:', start, '+', end)
        print()
        query &= Q(date__gte=start.strftime('%Y-%m-%d'), date__lte=end.strftime('%Y-%m-%d'))

    if search_month_receipt:
        print('month:', search_month_receipt[0:2])
        print('year:', search_month_receipt[3:7])
        month = datetime.strptime(search_month_receipt[0:2], '%m').date()
        year = datetime.strptime(search_month_receipt[3:7], '%Y').date()
        query &= Q(date__month=month.strftime('%m'), date__year=year.strftime('%Y'))

    if search_flat_receipt:
        query &= Q(appartament__number_appartament__icontains=search_flat_receipt)

    if search_owner_receipt:
        query &= Q(appartament__owner_id=search_owner_receipt)

    if search_confirm_receipt:
        print('+-+-+', search_confirm_receipt)
        if search_confirm_receipt == 'Не проведена':
            query &= Q(confirm=False)
        else:
            query &= Q(confirm=True)

    receipts = receipts.filter(query)

    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))

    paginator = Paginator(receipts, length)
    receipts = paginator.get_page(start // length + 1)

    data = []

    for receipt in receipts:
        service = ServiceforTariif.objects.get(tarrif_id=receipt.tarrif.id)
        data.append({
            'id': receipt.id,
            'num': receipt.uid,
            'status': receipt.get_status_pay_display(),
            'date': receipt.date.strftime('%d.%m.%Y'),
            'month': receipt.date.strftime(ukrainian_month_name + ' %Y'),
            'flat': receipt.appartament.number_appartament,
            'owner': receipt.appartament.owner.get_full_name(),
            'confirm': receipt.confirm,
            'suma': service.price * service.consum
        })

    response = {
        'draw': request.GET.get('draw'),
        'recordsTotal': Receipt.objects.all().count(),
        'recordsFiltered': receipts.paginator.count,
        'data': data
    }

    return JsonResponse(response)


def delete_selected_receipt(request):
    receipt_items = request.POST.getlist('selectedItems[]')

    for item_id in receipt_items:
        Receipt.objects.filter(id=item_id).delete()

    return redirect('ReceiptList')


def check_receipt_measure(request):
    print(request.GET.get('service_id'))
    if request.GET.get('service_id') != '' and request.GET.get('service_id') is not None:
        print('Works')
        measure = serializers.serialize('json', Service.objects.filter(pk=request.GET.get('service_id')))
        all_measure = serializers.serialize('json', Measure.objects.all())
        price = serialize('json', ServiceforTariif.objects.filter(service_id=request.GET.get('service_id')))
        return JsonResponse({'measure': measure, 'all_measure': all_measure, 'price': price}, status=200)
    else:
        print('Zero to hero')
        return JsonResponse({'measure': 0, 'all_measure': 0}, status=200)



def all_service_for_tarrif(request):
    tarrif = ServiceforTariif.objects.filter(tarrif_id=3)
    print(tarrif)
    tariffs = serialize('json', ServiceforTariif.objects.filter(tarrif_id=request.GET.get('tariff_id')))
    services = serialize('json', Service.objects.all())
    return JsonResponse({'tariffs': tariffs, 'services': services}, status=200)


def add_meter_data(request):
    house_id = request.GET.get('house_id')
    section_id = request.GET.get('section_id')
    flat_id = request.GET.get('appartament_id')
    meter_id = json.loads(request.GET.get('meter_id'))
    price = json.loads(request.GET.get('price'))
    if house_id == '' or section_id == '' or flat_id == '':
        return JsonResponse({'text': 'Не всі дані вказано'})
    else:
        for i in range(len(meter_id)):
            MetersData.objects.create(
                uid=random.randint(1, 1000),
                status='Нове',
                house_id=house_id,
                section_id=section_id,
                appartament_id=flat_id,
                meter_id=meter_id[i],  # Використовуємо числовий індекс
                meters_data=price[i],  # Використовуємо числовий індекс
                date_published=datetime.now()
            )
        return JsonResponse({'text': 'Лічильникі записано та додано'})





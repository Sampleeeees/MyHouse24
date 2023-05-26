import json

from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from Personal_book.models import *
from .forms import PersonalBookForm
from openpyxl import Workbook
from django.http import HttpResponse
from Statement.models import Statement
from Appartament.models import Appartament
from Receipt.models import Receipt
from Tarrif_and_services.models import ServiceforTariif
# Create your views here.

class PersonalList(ListView):
    model = PersonalBook
    template_name = 'Personal_book/personal_list.html'
    queryset = PersonalBook.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PersonalList, self).get_context_data(**kwargs)
        context['houses'] = House.objects.all()
        context['owners'] = User.objects.filter(appartament__isnull=False).distinct()
        context['all_book'] = PersonalBook.objects.all().count()

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


class PersonalCreate(CreateView):
    model = PersonalBook
    template_name = 'Personal_book/personal_create.html'
    form_class = PersonalBookForm
    success_url = reverse_lazy('PersonalList')

    def get_context_data(self, **kwargs):
        context = super(PersonalCreate, self).get_context_data(**kwargs)
        context['owner'] = User.objects.filter(appartament__id=self.request.POST.get('appartament'))
        return context
    def form_valid(self, form):
        context = self.get_context_data(form=form)
        user = form.save(commit=False)
        user.owner = context['owner'][0]
        user.save()

        return super().form_valid(form=form)

class PersonalUpdate(UpdateView):
    model = PersonalBook
    template_name = 'Personal_book/personal_update.html'
    form_class = PersonalBookForm
    success_url = reverse_lazy('PersonalList')

    def get_context_data(self, **kwargs):
        context = super(PersonalUpdate, self).get_context_data(**kwargs)
        context['owner'] = User.objects.filter(appartament__id=self.request.POST.get('appartament'))
        context['appartament'] = Appartament.objects.filter(id=self.request.POST.get('appartament'))
        context['uid'] = self.request.POST.get('uid')
        print('uid', self.request.POST.get('uid'))
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        user = form.save(commit=False)
        user.owner = context['owner'][0]
        user.appartament = context['appartament'][0]
        user.uid = context['uid']
        user.save()

        return super().form_valid(form=form)


class PersonalDelete(DeleteView):
    model = PersonalBook
    success_url = reverse_lazy('PersonalList')

    def get(self, request, *args, **kwargs):
        return self.delete(self, request, *args, **kwargs)


def personal_book_list(request):
    personals = PersonalBook.objects.all()

    #Search
    search_personal_num = request.GET.get('personal_num')
    search_personal_status = request.GET.get('personal_status')
    search_personal_flat = request.GET.get('personal_flat')
    search_personal_house = request.GET.get('personal_house')
    search_personal_section = request.GET.get('personal_section')
    search_personal_owner = request.GET.get('personal_owner')
    search_personal_residual = request.GET.get('personal_residual')

    query = Q()

    if search_personal_num:
        query &= Q(uid__icontains=search_personal_num)

    if search_personal_status:
        query &= Q(status=search_personal_status)

    if search_personal_flat:
        query &= Q(appartament__number_appartament__icontains=search_personal_flat)

    if search_personal_house:
        query &= Q(house_id=search_personal_house)

    if search_personal_section:
        query &= Q(section_id=search_personal_section)

    if search_personal_owner:
        query &= Q(owner_id=search_personal_owner)

    if search_personal_residual:
        query &= Q(residual__icontains=search_personal_residual)

    personals = personals.filter(query)

    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))

    paginator = Paginator(personals, length)
    personals = paginator.get_page(start // length + 1)

    data = []

    for personal in personals:
        data.append({
            'id': personal.id,
            'num': personal.uid,
            'status': personal.get_status_display(),
            'flat': personal.appartament.number_appartament,
            'house': personal.house.name_home,
            'section': personal.section.name_section,
            'owner': personal.owner.get_full_name(),
            'residual': personal.residual
        })

    response = {
        'draw': request.GET.get('draw'),
        'recordsTotal': PersonalBook.objects.all().count(),
        'recordsFiltered': personals.paginator.count,
        'data': data
    }

    return JsonResponse(response)


def filter_house_personal(request):
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

def filter_appartament_personal(request):
    if request.GET.get('house_id') != '' and request.GET.get('section_id') != '':
        appartaments = serialize('json', Appartament.objects.filter(house_id=request.GET.get('house_id'), section_id=request.GET.get('section_id')), use_natural_foreign_keys=True)
        return JsonResponse({'appartaments': appartaments}, status=200)
    else:
        return JsonResponse({}, status=200)


def appartament_detail(request):
    if request.GET.get('flat_id') != '' and request.GET.get('flat_id') is not None:
        owner_name = serialize('json', User.objects.filter(appartament__id=request.GET.get('flat_id')))
        return JsonResponse({'owner': owner_name}, status=200)
    else:
        return JsonResponse({}, status=200)


def export_to_excel(request):
    # Отримати відфільтровані дані з DataTable
    filtered_data = request.POST.get('filtered_data') # Припустимо, що дані передаються в POST-запиті у форматі JSON
    data = json.loads(filtered_data) # Перетворюємо рядок JSON у масив об'єктів

    # Створити новий файл Excel
    wb = Workbook()

    # Додати аркуш до файлу Excel
    ws = wb.active

    # Записати дані у файл Excel
    for row in data:
        ws.append(row)

    # Зберегти файл Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=my_excel_file.xlsx'
    wb.save(response)
    return response
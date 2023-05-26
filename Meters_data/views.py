from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.db.models import Q
from django.http import JsonResponse
from .forms import MeterForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from House.models import House, Section
from Tarrif_and_services.models import Service

from Meters_data.models import MetersData
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
# Create your views here.

class MeterDataList(ListView):
    model = MetersData
    template_name = 'Meters_data/meter_data_list.html'
    queryset = MetersData.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MeterDataList, self).get_context_data(**kwargs)
        context['houses'] = House.objects.all()
        context['sections'] = Section.objects.all()
        context['meters'] = Service.objects.filter(status_view=True)
        return context


class MeterDataCreate(CreateView):
    model = MetersData
    template_name = 'Meters_data/meter_data_create.html'
    success_url = reverse_lazy('Meter_data_list')
    form_class = MeterForm

    def get_context_data(self, **kwargs):
        context = super(MeterDataCreate, self).get_context_data(**kwargs)
        context['houses'] = House.objects.all()
        context['meters'] = Service.objects.filter(status_view=True)
        return context

    def form_valid(self, form):
        checking = self.request.POST == 'action_save_add'
        print(checking)
        if self.request.POST.get('action_save'):
            form.save()
            print('Action save')
            return redirect('Meter_data_list')
        elif self.request.POST.get('action_save_add'):
            form.save()
            print('Action add save')
            return redirect('Meter_data_create')

class MeterDataCopy(CreateView):
    model = MetersData
    template_name = 'Meters_data/meter_data_copy.html'
    form_class = MeterForm
    success_url = reverse_lazy('meter_data_list')

    def get_initial(self):
        # Отримання початкових значень для форми копіювання тарифу
        meter_data = MetersData.objects.get(pk=self.kwargs['pk'])
        initial = {
            'uid': meter_data.uid + 1,  # Замініть field1 на реальні поля моделі Tarrif, які потрібно скопіювати
            'date_published': meter_data.date_published,
            'house': meter_data.house,
            'section': meter_data.section,
            'appartament': meter_data.appartament,
            'meter': meter_data.meter,
            'status': meter_data.status,


            # Додайте інші поля моделі, які потрібно скопіювати
        }
        return initial

    def get_context_data(self, **kwargs):
        context = super(MeterDataCopy, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        context['houses'] = House.objects.all()
        context['meters'] = Service.objects.filter(status_view=True)
        return context

    def form_valid(self, form):
        checking = self.request.POST == 'action_save_add'
        print(checking)
        if self.request.POST.get('action_save'):
            form.save()
            print('Action save')
            return redirect('Meter_data_list')
        elif self.request.POST.get('action_save_add'):
            form.save()
            print('Action add save')
            return redirect('Meter_data_create')


class MeterDataSortList(ListView):
    model = MetersData
    template_name = 'Meters_data/meter_sort_list.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MeterDataSortList, self).get_context_data(**kwargs)
        context['houses'] = House.objects.all()
        context['sections'] = Section.objects.all()
        context['meters'] = Service.objects.filter(status_view=True)
        return context

class MeterDataUpdate(UpdateView):
    model = MetersData
    template_name = 'Meters_data/meter_data_update.html'
    form_class = MeterForm
    success_url = reverse_lazy('Meter_data_list')

    def get_context_data(self, **kwargs):
        context = super(MeterDataUpdate, self).get_context_data(**kwargs)
        context['houses'] = House.objects.all()
        context['meters'] = Service.objects.filter(status_view=True)
        return context

    def form_valid(self, form):
        checking = self.request.POST == 'action_save_add'
        print(checking)
        if self.request.POST.get('action_save'):
            form.save()
            print('Action save')
            return redirect('Meter_data_list')
        elif self.request.POST.get('action_save_add'):
            form.save()
            print('Action add save')
            return redirect('Meter_data_create')



class MeterDataDelete(DeleteView):
    model = MetersData
    success_url = reverse_lazy('Meter_data_list')

    def get(self, request, *args, **kwargs):
        return self.delete(self, request, *args, **kwargs)


def meter_data_list(request):
    meters = MetersData.objects.all()

    #SEARCH
    search_meter_home = request.GET.get('meter_home')
    search_meter_section = request.GET.get('meter_section')
    search_meter_flat_num = request.GET.get('meter_flat_num')
    search_meter_meter = request.GET.get('meter_meter')

    query = Q()

    if search_meter_home:
        query &= Q(house_id=search_meter_home)

    if search_meter_section:
        query &= Q(section_id=search_meter_section)

    if search_meter_flat_num:
        query &= Q(appartament__number_appartament__icontains=search_meter_flat_num)

    if search_meter_meter:
        query &= Q(meter_id=search_meter_meter)

    meters = meters.filter(query).order_by('pk')


    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))

    paginator = Paginator(meters, length)
    meters = paginator.get_page(start // length + 1)

    data = []

    for meter in meters:
        data.append({
            'id': meter.id,
            'home': meter.house.name_home,
            'section': meter.section.name_section,
            'flat': meter.appartament.number_appartament,
            'meter': f'{meter.meter.service} ({meter.meter.id})',
            'ost': meter.meters_data,
            'measure': meter.meter.measure.name_measure
        })

    response = {
        'draw': request.GET.get('draw'),
        'recordsTotal': MetersData.objects.all().count(),
        'recordsFiltered': meters.paginator.count,
        'data': data
    }

    return JsonResponse(response)

def filter_house_meter(request):
    print(request.GET.get('house_id'))
    if request.GET.get('house_id') != '' and request.GET.get('house_id') is not None:
        print('Hello')
        sections = serialize('json', Section.objects.filter(house_id=request.GET.get('house_id')))
        return JsonResponse({'sections': sections}, status=200)
    else:
        print('Not Working')
        return JsonResponse({}, status=200)

def meter_sort_data(request):
    meters = MetersData.objects.all()

    #SEARCH
    search_meter_uid = request.GET.get('meter_uid')
    search_meter_status = request.GET.get('meter_status')
    search_meter_date = request.GET.get('meter_date')
    search_meter_month = request.GET.get('meter_month')
    search_meter_home = request.GET.get('meter_home')
    search_meter_section = request.GET.get('meter_section')
    search_meter_flat_num = request.GET.get('meter_flat_num')
    search_meter_meter = request.GET.get('meter_meter')

    query = Q()

    if search_meter_uid:
        query &= Q(uid__icontains=search_meter_uid)

    if search_meter_status:
        query &= Q(status=search_meter_status)

    if search_meter_date:
        query &= Q(date_published=search_meter_date)

    if search_meter_month:
        query &= Q(date_published=search_meter_month)

    if search_meter_home:
        query &= Q(house_id=search_meter_home)

    if search_meter_section:
        query &= Q(section_id=search_meter_section)

    if search_meter_flat_num:
        query &= Q(appartament__number_appartament__icontains=search_meter_flat_num)

    if search_meter_meter:
        query &= Q(meter_id=search_meter_meter)

    meters = meters.filter(query).order_by('pk')


    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))

    paginator = Paginator(meters, length)
    meters = paginator.get_page(start // length + 1)

    data = []

    for meter in meters:
        data.append({
            'id': meter.id,
            'uid': meter.uid,
            'status': meter.get_status_display(),
            'date': meter.date_published,
            'month': meter.date_published,
            'home': meter.house.name_home,
            'section': meter.section.name_section,
            'flat': meter.appartament.number_appartament,
            'meter': meter.meter.service,
            'ost': meter.meters_data,
            'measure': meter.meter.measure.name_measure
        })

    response = {
        'draw': request.GET.get('draw'),
        'recordsTotal': MetersData.objects.all().count(),
        'recordsFiltered': meters.paginator.count,
        'data': data
    }

    return JsonResponse(response)
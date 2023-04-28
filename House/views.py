import requests
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import House, Floor, Section
from .forms import HouseForm, FloorForm, SectionForm
from Gallery.forms import GalleryForm, ImageForm
from Gallery.models import Gallery, Image
from django.forms import modelformset_factory
# Create your views here.

class HouseList(ListView):
    model = House
    template_name = 'House/house_list.html'
    queryset = House.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HouseList, self).get_context_data(**kwargs)
        print(self.request.POST)
        context['count_house'] = House.objects.all().count()
        return context

class HouseCreate(CreateView):
    model = House
    template_name = 'House/house_create.html'
    form_class = HouseForm
    success_url = reverse_lazy('house_list')


    def get_context_data(self, **kwargs):
        context = super(HouseCreate, self).get_context_data(**kwargs)
        SectionFormset = modelformset_factory(Section, form=SectionForm, extra=0, can_delete=True)
        FloorFormset = modelformset_factory(Floor, form=FloorForm, extra=0, can_delete=True)
        if self.request.POST:
            context['formset_section'] = SectionFormset(self.request.POST, self.request.FILES, prefix='section', queryset=Section.objects.none())
            context['formset_floor'] = FloorFormset(self.request.POST, self.request.FILES, prefix='floor', queryset=Floor.objects.none())
        else:
            context['formset_section'] = SectionFormset(prefix='section', queryset=Section.objects.none())
            context['formset_floor'] = FloorFormset(prefix='floor', queryset=Section.objects.none())
        return context


    def form_valid(self, form, **kwargs):
        print(form)
        context = self.get_context_data(form=form, **kwargs)
        house = form.save()
        if context['formset_section'].is_valid() and context['formset_floor'].is_valid():
            for section in context['formset_section']:
                sec = section.save(commit=False)
                sec.house_id = house.id
                sec.save()
            context['formset_section'].save()
            for floor in context['formset_floor']:
                fl = floor.save(commit=False)
                fl.house_id = house.id
                fl.save()
            context['formset_floor'].save()
        else:
            print(context['formset_section'].errors)

        # context['formset_section'].save()
        return super().form_valid(form)


class HouseUpdate(UpdateView):
    model = House
    template_name = 'House/house_update.html'
    form_class = HouseForm
    success_url = reverse_lazy('house_list')

    def get_context_data(self, **kwargs):
        context = super(HouseUpdate, self).get_context_data(**kwargs)
        print(context['house'].id)
        SectionFormset = modelformset_factory(Section, form=SectionForm, extra=0, can_delete=True)
        FloorFormset = modelformset_factory(Floor, form=FloorForm, extra=0, can_delete=True)
        if self.request.POST:
            context['formset_section'] = SectionFormset(self.request.POST, self.request.FILES, prefix='section',
                                                        queryset=Section.objects.filter(house=context['house'].id))
            context['formset_floor'] = FloorFormset(self.request.POST, self.request.FILES, prefix='floor',
                                                    queryset=Floor.objects.filter(house=context['house'].id))
        else:
            context['formset_section'] = SectionFormset(prefix='section', queryset=Section.objects.filter(house=context['house'].id))
            context['formset_floor'] = FloorFormset(prefix='floor', queryset=Floor.objects.filter(house=context['house'].id))
        return context

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(form=form, **kwargs)
        house = context['house']
        for section in context['formset_section']:
            sec = section.save(commit=False)
            sec.house_id = house.id
            sec.save()
        context['formset_section'].save()
        for floor in context['formset_floor']:
            fl = floor.save(commit=False)
            fl.house_id = house.id
            fl.save()
        context['formset_floor'].save()

        return super().form_valid(form)


class HouseDetail(DetailView):
    model = House
    template_name = 'House/house_detail.html'


    def get_context_data(self, **kwargs):
        context = super(HouseDetail, self).get_context_data(**kwargs)
        context['sections'] = Section.objects.filter(house_id=context['object'].id).count()
        context['floors'] = Floor.objects.filter(house_id=context['object'].id).count()
        return context

def delete_item(request, pk):
    House.objects.filter(pk=pk).delete()
    return redirect('house_list')


def house_list(request):
    houses = House.objects.all()

    search_name_home = request.GET.get('search_name_home')
    search_address = request.GET.get('search_home_address')

    print(search_address, search_name_home)

    filter_name_home = request.GET.get('filter_name_home')
    filter_home_address = request.GET.get('filter_home_address')

    print(filter_home_address, filter_home_address)

    query = Q()

    if search_name_home:
        query &= Q(name_home__icontains=search_name_home)

    if search_address:
        query &= Q(address__icontains=search_address)

    houses = houses.filter(query)


    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))


    paginator = Paginator(houses, length)
    houses = paginator.get_page(start // length + 1)

    data = []

    for house in houses:
        data.append({
            'id': house.id,
            'name_home': house.name_home,
            'address': house.address
        })


    response = {
        'draw': request.GET.get('draw'),
        'recordsTotal': House.objects.count(),
        'recordsFiltered': houses.paginator.count,
        'data': data
    }

    return JsonResponse(response)


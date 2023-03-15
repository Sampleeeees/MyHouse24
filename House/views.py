import requests
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView
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

def delete_item(request, pk):
    House.objects.filter(pk=pk).delete()
    return redirect('house_list')




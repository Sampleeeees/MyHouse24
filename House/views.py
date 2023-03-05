from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic import View, CreateView, ListView
from .models import House, Floor, Section
from .forms import HouseForm
from Gallery.forms import GalleryForm, ImageForm
from Gallery.models import Gallery
# Create your views here.

class HouseList(ListView):
    model = House
    template_name = 'House/house_list.html'
    queryset = House.objects.all()

class HouseCreate(CreateView):
    model = House
    template_name = 'House/house_create.html'
    form_class = HouseForm
    context_object_name = 'home'
    template_name_suffix = '_home'
    template_name_field = 'home'
    def form_valid(self, form):
        print(form.cleaned_data)
        print(form.error_class)
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = HouseForm(request.POST or None, request.FILES or None)
        imageForm = ImageForm(request.POST or None, request.FILES or None)
        if imageForm.is_valid() and form.is_valid():
            house = form.save(commit=False)
            print(imageForm.cleaned_data)
            form = imageForm.save(commit=False)
            gallery = Gallery.objects.create(text='House')
            form.gallery = get_object_or_404(Gallery, pk=gallery.id)
            house.gallery = get_object_or_404(Gallery, pk=gallery.id)
            form.save()
            house.save()
            return redirect('house_list')
        else:
            print(form.errors, imageForm.errors)
            return HttpResponse('not Valid')

class FloorCreate(CreateView):
    model = Floor
    template_name = 'House/house_create.html'
    fields = ['name_floor']
    template_name_suffix = 'floor'
    print(template_name_suffix)




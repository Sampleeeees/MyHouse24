from django import forms
from django.forms import ModelForm
from .models import House, Section, Floor
from Gallery.forms import GalleryForm, ImageForm


class HouseForm(ModelForm):
    image = ImageForm
    gallery = GalleryForm
    class Meta:
        model = House
        fields = ['name_home', 'address', 'floor', 'section', 'staff', 'gallery']
        widgets = {
            'name_home': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }


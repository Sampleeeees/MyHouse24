from django import forms
from django.forms import ModelForm
from .models import Gallery, Image

class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ['text']

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        widgets = {
            'image': forms.FileInput()
        }
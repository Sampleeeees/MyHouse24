from django import forms
from django.forms import ModelForm
from .models import GeneralPage, AboutUs, SeoBlock, BlockAndServices, Contacts

class SeoBlockForm(ModelForm):
    class Meta:
        model = SeoBlock
        fields = ['title_seo', 'description_seo', 'keywords_seo']
        widgets = {
            'title_seo': forms.TextInput(attrs={'class': 'form-control'}),
            'description_seo': forms.Textarea(attrs={'class': 'form-control'}),
            'keywords_seo': forms.Textarea(attrs={'class': 'form-control'})
        }


class BlockAndServicesForm(ModelForm):
    class Meta:
        model = BlockAndServices
        fields = ['image', 'title', 'description']
        widgets = {
            'image': forms.FileInput(),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control h-50'}),
        }


class GeneralPageForm(ModelForm):
    class Meta:
        model = GeneralPage
        fields = ['title', 'short_text', 'image1', 'image2', 'image3']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'short_text': forms.Textarea(attrs={'class': 'form-control'}),
        }
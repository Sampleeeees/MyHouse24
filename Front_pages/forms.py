from django import forms
from django.forms import ModelForm
from .models import GeneralPage, AboutUs, SeoBlock, BlockAndServices, Contacts, Document, Services, PageTarrif, TarrifForm

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
            'image': forms.FileInput(attrs={'onchange': 'add_image(this, "img-block-__prefix__")'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control h-50'}),
        }

class ServicesForm(ModelForm):
    class Meta:
        model = Services
        fields = ['name']


class GeneralPageForm(ModelForm):
    class Meta:
        model = GeneralPage
        fields = ['title', 'short_text', 'image1', 'image2', 'image3']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'short_text': forms.Textarea(attrs={'class': 'form-control'}),
            'image1': forms.FileInput(attrs={'onchange': 'add_image(this, "image-1-page")'}),
            'image2': forms.FileInput(attrs={'onchange': 'add_image(this, "image-2-page")'}),
            'image3': forms.FileInput(attrs={'onchange': 'add_image(this, "image-3-page")'}),
        }

class AboutUsForm(ModelForm):
    class Meta:
        model = AboutUs
        fields = ['title', 'title_sec', 'short_text', 'short_text_sec', 'image_director']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_sec': forms.TextInput(attrs={'class': 'form-control'}),
            'short_text': forms.Textarea(attrs={'class': 'form-control'}),
            'short_text_sec': forms.Textarea(attrs={'class': 'form-control'}),
            'image_director': forms.FileInput(attrs={'onchange': 'add_image(this, "DirectorImage")'})
        }

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ['document', 'text']
        widgets = {
            'document': forms.FileInput(),
            'text': forms.TextInput(attrs={'class':'form-control'})
        }

class ContactsForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ['title', 'short_text', 'link', 'fio', 'email', 'location', 'phone_number', 'code_card', 'address']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'short_text': forms.Textarea(attrs={'class': 'form-control'}),
            'fio': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'code_card': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PageTarrifForm(ModelForm):
    class Meta:
        model = PageTarrif
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }
class TarrifFormForm(ModelForm):
    class Meta:
        model = TarrifForm
        fields = ['title', 'image']
        widgets = {
            'image': forms.FileInput(attrs={'onchange': 'add_image(this, "img-block-__prefix__")'}),
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }
from django import forms
from django.forms import ModelForm
from .models import Service, Tarrif, Measure, ServiceforTariif

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['service', 'status_view', 'measure']
        widgets = {
            'service': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-size: 14px;'}),
            'measure': forms.Select(attrs={'class': 'form-select'})
        }

class TarrifForm(ModelForm):
    class Meta:
        model = Tarrif
        fields = ['name_tarrif', 'description_tarrif']
        widgets = {
            'name_tarrif': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-size: 14px;'}),
            'description_tarrif': forms.Textarea(attrs={'class': 'form-control', 'style': 'font-size: 14px;'}),
        }

class MeasureForm(ModelForm):
    class Meta:
        model = Measure
        fields = ['name_measure']
        widgets = {
            'name_measure': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-size: 14px;'})
        }

class ServiceforTariifForm(ModelForm):
    class Meta:
        model = ServiceforTariif
        fields = ['tarrif', 'service', 'amount']
        widgets = {
            'service': forms.Select(attrs={'class': 'form-select', 'onchange': 'select_measure(this)', 'id': 'service_select'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'})
        }


from django import forms
from django.forms import ModelForm
from .models import Receipt

class ReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        fields = ['confirm', 'date_created', 'status_pay', 'tarrif', 'appartament', 'uid']
        widgets = {
            'tarrif': forms.Select(attrs={'class': 'form-select'}),
            'appartament': forms.Select(attrs={'class': 'form-select'}),
        }
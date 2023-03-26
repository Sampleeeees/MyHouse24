from django.forms import ModelForm
from django import forms
from .models import *

class PaymentForm(ModelForm):
    class Meta:
        model = PaymentDetail
        fields = ['name_company', 'information']
        widgets = {
            'name_company': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-size: 14px;'}),
            'information': forms.Textarea(attrs={'class': 'form-control', 'style': 'font-size: 14px;'})
        }

Type_choice = {
    (None, 'Прихід'),
    (1000, 'Розхід')
}
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name_article', 'type']
        widgets = {
            'name_article': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-size: 14px;'}),\
            'type': forms.ChoiceField(choices=Type_choice)
        }
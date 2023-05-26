from django import forms
from django.forms import ModelForm
from .models import Receipt

class ReceiptForm(ModelForm):

    def __init__(self, **kwargs):
        super(ReceiptForm, self).__init__(**kwargs)

        self.fields['tarrif'].empty_label = 'Оберіть...'
        self.fields['tarrif'].label_from_instance = lambda obj: "%s" %(obj.name_tarrif)

        self.fields['appartament'].empty_label = 'Оберіть...'
        self.fields['appartament'].label_from_instance = lambda obj: "%s" % (obj.number_appartament)

        self.fields['house'].empty_label = 'Оберіть...'
        self.fields['house'].label_from_instance = lambda obj: "%s" % (obj.name_home)

        self.fields['section'].empty_label = 'Оберіть...'
        self.fields['section'].label_from_instance = lambda obj: "%s" % (obj.name_section)
    class Meta:
        model = Receipt
        fields = ['confirm', 'date', 'status_pay', 'tarrif', 'appartament', 'uid', 'house', 'section', 'personal_book', 'start_date', 'end_date']
        widgets = {
            'confirm': forms.CheckboxInput(attrs={'class': 'checkbutton'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker', 'autocomplete': 'off'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control w-50', 'id': 'datepicker1', 'autocomplete': 'off'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control w-50', 'id': 'datepicker2', 'autocomplete': 'off'}),
            'uid': forms.TextInput(attrs={'class': 'form-control'}),
            'tarrif': forms.Select(attrs={'class': 'form-select has-select-wait'}),
            'appartament': forms.Select(attrs={'class': 'form-select', 'disabled': '', 'id': 'id_appartament_select'}),
            'house': forms.Select(attrs={'class': 'form-select has-select-wait', 'id': 'id_house_select'}),
            'section': forms.Select(attrs={'class': 'form-select', 'disabled': '', 'id': 'id_section_select'}),
            'personal_book': forms.TextInput(attrs={'class': 'form-control'}),
            'status_pay': forms.Select(attrs={'class': 'form-select has-select-wait'}),
        }
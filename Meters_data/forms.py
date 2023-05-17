from django import forms
from django.forms import ModelForm

from .models import MetersData

class MeterForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(MeterForm, self).__init__(*args, **kwargs)

        self.fields['house'].empty_label = 'Оберіть...'
        self.fields['house'].label_from_instance = lambda obj: "%s" % (obj.name_home)

        self.fields['section'].empty_label = 'Оберіть будинок...'
        self.fields['section'].label_from_instance = lambda obj: "%s" % (obj.name_section)

        self.fields['appartament'].empty_label = 'Оберіть будинок...'
        self.fields['appartament'].label_from_instance = lambda obj: "%s, %s" % (obj.number_appartament, obj.house.name_home)

        self.fields['meter'].empty_label = 'Оберіть...'
        self.fields['status'].empty_value = 'Пусто'

    class Meta:
        model = MetersData
        fields = ['uid', 'meter', 'meters_data', 'date_published', 'status', 'house', 'appartament', 'section']
        widgets = {
            'uid': forms.NumberInput(attrs={'class': 'form-control'}),
            'house': forms.Select(attrs={'class': 'form-select has-select-wait', 'id': 'id_house_select'}),
            'appartament': forms.Select(attrs={'class': 'form-select', 'disabled': '', 'title': 'Спочатку оберіть будинок та секцію', 'id': 'id_appartament_select'}),
            'section': forms.Select(attrs={'class': 'form-select', 'disabled': '', 'title': 'Спочатку оберіть будинок', 'id': 'id_section_select' }),
            'meter': forms.Select(attrs={'class': 'form-select has-select-wait'}),
            'meters_data': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select has-select-wait'}),
            'date_published': forms.DateInput(attrs={'class': 'form-control'})

        }
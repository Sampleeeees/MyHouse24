from django import forms
from django.forms import ModelForm
from .models import *

class AppartamentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppartamentForm, self).__init__(*args, **kwargs)
        #house
        self.fields['house'].empty_label = 'Оберіть...'
        self.fields['house'].label_from_instance = lambda obj: "%s" % (obj.name_home)
        #floor
        self.fields['floor'].empty_label = 'Оберіть...'
        self.fields['floor'].label_from_instance = lambda obj: "%s" %(obj.name_floor)
        #section
        self.fields['section'].empty_label = 'Оберіть...'
        self.fields['section'].label_from_instance = lambda obj: "%s" %(obj.name_section)
        #tarrif
        self.fields['tarrif'].empty_label = 'Оберіть...'
        self.fields['tarrif'].queryset = Tarrif.objects.all().order_by('-pk')
        self.fields['tarrif'].label_from_instance = lambda obj: "%s" %(obj.name_tarrif)
        #owner
        self.fields['owner'].empty_label = 'Оберіть...'
        self.fields['owner'].queryset = User.objects.all().order_by('-pk')
        self.fields['owner'].label_from_instance = lambda obj: "%s %s %s" %(obj.first_name, obj.middle_name, obj.last_name)
    class Meta:
        model = Appartament
        fields = ['number_appartament', 'area', 'house', 'section', 'floor', 'tarrif', 'owner']
        widgets = {
            'number_appartament': forms.TextInput(attrs={'class': 'form-control', 'id': 'number_appartament_id', 'disabled': ''}),
            'area': forms.NumberInput(attrs={'class': 'form-control'}),
            'house': forms.Select(attrs={'class': 'form-select', 'id': 'id_house_select'}),
            'section': forms.Select(attrs={'class': 'form-select', 'id': 'id_section_select', 'disabled': ''}),
            'floor': forms.Select(attrs={'class': 'form-select', 'id': 'id_floor_select', 'disabled': ''}),
            'tarrif': forms.Select(attrs={'class': 'form-select', 'id': 'id_tarrif_select'}),
            'owner': forms.Select(attrs={'class': 'form-select', 'id': 'id_owner_select'})
        }



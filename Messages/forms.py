from django.forms import ModelForm
from django import forms

import House.models
from .models import Message

class MessageForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['house'].empty_label = 'Оберіть...'
        self.fields['house'].label_from_instance = lambda obj: "%s" % (obj.name_home)

        self.fields['section'].empty_label = 'Оберіть...'
        self.fields['section'].label_from_instance = lambda obj: "%s" % (obj.name_section)

        self.fields['floor'].empty_label = 'Оберіть...'
        self.fields['floor'].label_from_instance = lambda obj: "%s" % (obj.name_floor)

        self.fields['appartament'].empty_label = 'Оберіть...'
    class Meta:
        model = Message
        fields = ['title_mess', 'description_mess', 'house', 'section', 'floor', 'appartament', 'date_send', 'user_send']
        widgets = {
            'title_mess': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'check_text_new(this)'}),
            'description_mess': forms.Textarea(attrs={'class': 'form-control', 'onkeyup': 'check_text_new(this)'}),
            'house': forms.Select(attrs={'class': 'form-select required', 'id': 'id_house_select', 'required': ''}),
            'section': forms.Select(attrs={'class': 'form-select required', 'disabled': '', 'id': 'id_section_select', 'required': ''}),
            'floor': forms.Select(attrs={'class': 'form-select', 'disabled': '', 'id': 'id_floor_select', 'required': ''}),
            'appartament': forms.Select(attrs={'class': 'form-select', 'disabled': '', 'id': 'id_appartament_select', 'required': ''}),
        }

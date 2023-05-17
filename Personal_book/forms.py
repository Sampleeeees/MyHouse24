from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
from .models import PersonalBook


class PersonalBookForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonalBookForm, self).__init__(*args, **kwargs)

        self.fields['house'].empty_label = 'Оберіть...'
        self.fields['house'].label_from_instance = lambda obj: "%s" %(obj.name_home)

        self.fields['section'].empty_label = 'Оберіть будинок...'
        self.fields['section'].label_from_instance = lambda obj: "%s" %(obj.name_section)

        self.fields['appartament'].empty_label = 'Оберіть будинок...'
        self.fields['appartament'].label_from_instance = lambda obj: "%s, %s" %(obj.number_appartament, obj.house.name_home)

    def clean_uid(self):
        uid = self.cleaned_data['uid']
        if not self.instance.pk:
            print('uid', uid)
            if PersonalBook.objects.filter(uid=uid).exists():
                raise ValidationError('Таке Uid вже існує')
            return uid

    def clean_appartament(self):
        if not self.instance.pk:
            flat = self.cleaned_data['appartament']
            if PersonalBook.objects.filter(appartament=flat).exists():
                raise ValidationError('Такий рахунок вже відкритий для квартири')
            return flat
    class Meta:
        model = PersonalBook
        fields = ['status', 'house', 'section', 'owner', 'appartament', 'residual', 'uid']
        widgets = {
            'uid': forms.NumberInput(attrs={'class': 'form-control', 'onkeyup': 'check_text_new(this)', 'required': ''}),
            'status': forms.Select(attrs={'class': 'form-select has-select-success'}),
            'house': forms.Select(attrs={'class': 'form-select has-select-wait', 'id': 'id_house_select'}),
            'owner': forms.Select(attrs={'class': 'form-select'}),
            'section': forms.Select(attrs={'class': 'form-select', 'disabled': '', 'title': 'Спочатку потрібно обрати будинок', 'id': 'id_section_select'}),
            'appartament': forms.Select(attrs={'class': 'form-select', 'disabled': '', 'title': 'Спочатку потрібно обрати секцію', 'id': 'id_appartament_select', 'name': 'user_id'}),
            'residual': forms.Select(attrs={'class': 'form-select'})
        }

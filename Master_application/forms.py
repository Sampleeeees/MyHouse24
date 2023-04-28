from django import forms
from django.forms import ModelForm
from .models import MatsterApplication, Type_Status
from User.models import User

class MasterForm(ModelForm):

    status = forms.ChoiceField(choices=Type_Status, initial='Нове')

    def __init__(self, *args, **kwargs):
        super(MasterForm, self).__init__(*args, **kwargs)
        #Empty_label for status
        self.fields['status'].widget.attrs.update({'class': 'form-select has-select-success' })
        self.fields['status'].empty_label = 'Оберіть...'
        self.fields['ownerAppartament'].empty_label = 'Оберіть...'
        self.fields['ownerAppartament'].label_from_instance = lambda obj: "%s %s %s" %(obj.first_name, obj.middle_name, obj.last_name)
        self.fields['appartament'].empty_label = 'Оберіть...'
        self.fields['appartament'].label_from_instance = lambda obj: "%s %s" % (obj.number_appartament, obj.house.name_home)
        self.fields['typeMaster'].empty_label = 'Оберіть...'
        self.fields['typeMaster'].label_from_instance = lambda obj: "%s" %(obj.name)
        self.fields['name_master'].empty_label = 'Оберіть...'
        self.fields['name_master'].queryset = User.objects.filter(role__user__isnull=False)
        self.fields['name_master'].label_from_instance = lambda obj: "%s - %s %s" %(obj.role.name, obj.first_name, obj.last_name)

    class Meta:
        model = MatsterApplication
        fields = ['description_problem', 'comment', 'typeMaster', 'status', 'name_master', 'ownerAppartament', 'appartament', 'date_master', 'time_master']
        widgets = {
            'description_problem': forms.Textarea(attrs={'class': 'form-control', 'onkeyup': 'check_text_new(this)'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'onkeyup': 'check_text_new(this)'}),
            'typeMaster': forms.Select(attrs={'class': 'form-select has-select-wait'}),
            'ownerAppartament': forms.Select(attrs={'class': 'form-select has-select-wait'}),
            'name_master': forms.Select(attrs={'class': 'form-select has-select-wait'}),
            'appartament': forms.Select(attrs={'class': 'form-select', 'disabled': '', 'title': 'Оберіть спочатку квартиру'}),
            'date_master': forms.DateInput(attrs={'class': 'form-control'}),
            'time_master': forms.TimeInput(attrs={'class': 'form-control timepicker'})
        }
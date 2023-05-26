from django import forms
from django.forms import ModelForm
from .models import Statement
from User.models import User

class StatementForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(StatementForm, self).__init__(*args, **kwargs)

        self.fields['personal_book'].empty_label = 'Оберіть...'
        self.fields['personal_book'].label_from_instance = lambda obj: "%s" % (obj.uid)

        self.fields['ownerAppartemnt'].empty_label = 'Оберіть...'
        self.fields['ownerAppartemnt'].label_from_instance = lambda obj: "%s %s %s" %(obj.first_name, obj.middle_name, obj.last_name)
        self.fields['ownerAppartemnt'].queryset = User.objects.filter(appartament__isnull=False).distinct()

        self.fields['user_manager'].empty_label = 'Оберіть...'
        self.fields['user_manager'].label_from_instance = lambda obj: "%s %s %s" %(obj.first_name, obj.middle_name, obj.last_name)
        self.fields['user_manager'].queryset = User.objects.filter(role__name='Директор')

        self.fields['article'].empty_label = 'Оберіть...'
        self.fields['article'].label_from_instance = lambda obj: "%s" %(obj.name_article)

    class Meta:
        model = Statement
        fields = ['uid', 'amount', 'type', 'comment', 'status', 'date_published', 'user_manager', 'ownerAppartemnt', 'personal_book', 'article', 'status_perfom']
        widgets = {
            'uid': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'check_text(this)'}),
            'status_perfom': forms.CheckboxInput(attrs={'class': 'checkbutton'}),
            'date_published': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker', 'autocomplete': 'off', 'onckeyup': 'check_text(this)'}),
            'amount': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'check_text(this)'}),
            'ownerAppartemnt': forms.Select(attrs={'class': 'form-select has-select-wait'}),
            'user_manager': forms.Select(attrs={'class': 'form-select has-select-wait'}),
            'personal_book': forms.Select(attrs={'class': 'form-select has-select-wait'}),
            'article': forms.Select(attrs={'class': 'form-select has-select-wait'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'onkeyup': 'check_text(this)'})
        }
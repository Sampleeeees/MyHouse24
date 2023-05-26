from django import forms
from django.forms import ModelForm
from .models import Service, Tarrif, Measure, ServiceforTariif
from User.models import User, STATUS_CHOICES

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
        fields = ['tarrif', 'service', 'price', 'consum']
        widgets = {
            'service': forms.Select(attrs={'class': 'form-select', 'onchange': 'select_measure(this)', 'id': 'service_select'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'consum': forms.TextInput(attrs={'class': 'form-control', 'onchange': "multiplyAndSetPrice(this.id)"})
        }


class UserForm(ModelForm):
    password1 = forms.CharField(label='Password', required=False, widget=forms.PasswordInput(attrs={'class': 'form-control pass-value'}))
    password2 = forms.CharField(label='Password repeat', required=False, widget=forms.PasswordInput(attrs={'class': 'form-control pass-value'}))

    #Щоб користувач міг сам обрати собі id
    id = forms.IntegerField(label='ID', min_value=0)


    status = forms.ChoiceField(choices=STATUS_CHOICES, initial='2000')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        #Empty_label for status
        self.fields['status'].widget.attrs.update({'class': 'form-select', 'aria-label': '.form-select example', 'onchange': 'isSelect(this)'})
        self.fields['id'].widget.attrs.update({'class': 'form-control', 'onkeyup': 'check_text_new(this)'})

    def clean_id(self):
        id = self.cleaned_data.get('id')
        if User.objects.filter(id=id).exists():
            raise forms.ValidationError('Це id вже зайнято')
        return id

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password1', 'password2', 'birthday', 'viber', 'telegram', 'status', 'logo', 'about_user', 'middle_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'check_text_new(this)'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'check_text_new(this)'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'check_text_new(this)'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'onkeyup': 'isEmail(this.value)'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'onkeyup': 'check_text_new(this)'}),
            'viber': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'check_text_new(this)'}),
            'telegram': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'check_text_new(this)'}),
            'about_user': forms.Textarea(attrs={'class': 'form-control', 'onkeyup': 'check_text_new(this)'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'onkeyup': 'check_text_new(this)'}),
            'logo': forms.FileInput(attrs={'onchange': 'add_image(this, "new_owner_logo")'})
        }




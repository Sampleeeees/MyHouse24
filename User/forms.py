from django import forms
from django.forms import ModelForm
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'viber', 'telegram', 'phone_number', 'logo', 'email', 'birthday']
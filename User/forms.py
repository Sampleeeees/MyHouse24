from django import forms
from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class RegistrationForm(ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'viber', 'telegram', 'phone_number', 'logo', 'email', 'birthday', 'password']


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserCreationForm(ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль', 'onkeyup': 'check_text(this)', 'autocomplete': 'off'}))
    password2 = forms.CharField(label='Password repeat', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторіть Пароль', 'onkeyup': 'check_text(this)'}))

    class Meta:
        model = User
        fields = ['first_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ПІБ', 'onkeyup': 'check_text(this)'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'onkeyup': 'check_text(this)'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'viber', 'telegram', 'phone_number', 'logo', 'email', 'birthday', 'is_staff', 'is_superuser', 'password']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email або ID', 'onkeyup': 'check_text(this)', 'autocomplete': 'off'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль', 'onkeyup': 'check_text(this)'}))


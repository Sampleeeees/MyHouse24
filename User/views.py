from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import *
from .authenticate import EmailAuthBackend
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
UserModel = get_user_model()
from .tokens import account_activation_token


# Create your views here.
def register_request(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data['first_name'])
            fio = form.cleaned_data['first_name'].split()
            print(fio)
            if len(fio) == 3:
                if len(form.cleaned_data['password1']) >= 8:
                    user = form.save(commit=False)
                    user.first_name = fio[0]
                    user.middle_name = fio[1]
                    user.last_name = fio[2]
                    user.is_active = False
                    user.save()
                    current_site = get_current_site(request)
                    mail_subject = 'Activate your account.'
                    message = render_to_string('User/acc_active_email.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                    })
                    to_email = form.cleaned_data.get('email')
                    email = EmailMessage(
                        mail_subject, message, to=[to_email]
                    )
                    email.send()
                else:
                    return render(request, 'User/registration_invalid.html', context={'register_form': form, 'error': 'Пароль повинен складаться мінімум з  символів і мати хоча б одну букву та цифру'})
            else:
                return render(request, 'User/registration_invalid.html', context={'register_form': form, 'error': 'Уведіть повністю ПІБ'})

            print("Registration successful.")
            return render(request, 'User/confirm_registartion.html')
        print("Unsuccessful registration. Invalid information.")
        print(form.errors)
        return render(request, 'User/registration_invalid.html', context={'register_form': form, 'error': form.errors})
    form = UserCreationForm
    return render(request, template_name="User/registration.html", context={"register_form": form})

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='User.backends.EmailBackend')
        return redirect('house_list')
    else:
        return HttpResponse('Activation link is invalid!')

def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = EmailAuthBackend.authenticate(request, nickname=email, password=password)
            if user is not None and not user.is_superuser:
                login(request, user, backend='User.backends.EmailBackend')
                messages.info(request, f"You are now logged in as {email}.")
                return redirect("statistic")
            else:
                return render(request=request, template_name="User/login.html", context={"login_form": form, 'error': 'Не вірний логін або пароль'})
        else:
            return render(request=request, template_name="User/login.html", context={"login_form": form, 'error': 'Ведіть дані коректно'})
    form = LoginForm()
    return render(request=request, template_name="User/login.html", context={"login_form": form})


def login_request_admin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = EmailAuthBackend.authenticate(request, nickname=email, password=password)
            if user is not None and user.is_superuser:
                login(request, user, backend='User.backends.EmailBackend')
                messages.info(request, f"You are now logged in as {email}.")
                return redirect("statistic")
            else:
                return render(request=request, template_name="User/admin_login.html", context={"login_form": form, 'error': 'Не вірний пароль чи логін'})
        else:
            return render(request=request, template_name="User/admin_login.html", context={"login_form": form, 'error': 'Введіть дані коректно'})
    form = LoginForm()
    return render(request=request, template_name="User/admin_login.html", context={"login_form": form})

def logout_request(request):
    logout(request)
    return redirect("FrontGeneral")

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=250)
    director = models.BooleanField()
    manager = models.BooleanField()
    booker = models.BooleanField()
    electrician = models.BooleanField()
    plumber = models.BooleanField()
    slusar = models.BooleanField()


STATUS_CHOICES = (
    ('1000', 'Активний'),
    ('2000', 'Новий'),
    ('3000', 'Неактивний'))
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('first_name'), max_length=50)
    middle_name = models.CharField(_('middle_name'), max_length=50)
    last_name = models.CharField(_('last_name'), max_length=50)
    uid = models.IntegerField(blank=True, null=True)
    logo = models.ImageField(_('logo'), upload_to='user/logo/', blank=True)
    about_user = models.CharField(_('about_user'), max_length=500, blank=True, null=True)
    birthday = models.DateField(_('birthday'), blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.IntegerField(_('phone_number'), blank=True, null=True)
    viber = models.IntegerField(_('viber'), blank=True, null=True)
    telegram = models.CharField(_('telegram'), max_length=250, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    status = models.CharField(_('status'), max_length=50, choices=STATUS_CHOICES, null=True)
    is_staff = models.BooleanField(_('staff'), default=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_superuser = models.BooleanField(_('superuser'), default=False)
    role = models.ForeignKey(Role, null=True, verbose_name='Роль', on_delete=models.CASCADE)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'nickname']

    def get_full_name(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name



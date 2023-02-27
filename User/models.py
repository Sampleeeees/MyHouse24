from django.db import models

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=250)
    director = models.BooleanField()
    manager = models.BooleanField()
    booker = models.BooleanField()
    electrician = models.BooleanField()
    plumber = models.BooleanField()
    slusar = models.BooleanField()

class User(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='user/logo/', blank=True)
    birthday = models.DateField()
    phone_number = models.IntegerField()
    viber = models.IntegerField()
    telegram = models.CharField(max_length=250)
    email = models.EmailField()
    status = models.BooleanField()
    role = models.ForeignKey(Role, null=True, verbose_name='Роль', on_delete=models.CASCADE)


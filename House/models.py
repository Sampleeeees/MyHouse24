from django.db import models
from User.models import User
from Gallery.models import Gallery
# Create your models here.

class Floor(models.Model):
    name_floor = models.CharField(max_length=100)


class Section(models.Model):
    name_section = models.CharField(max_length=100)

class House(models.Model):
    name_home = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    floor = models.ForeignKey(Floor, verbose_name='Поверх', on_delete=models.CASCADE, blank=True)
    section = models.ForeignKey(Section, verbose_name='Секція', on_delete=models.CASCADE, blank=True)
    staff = models.ManyToManyField('User', related_name='Працівники у будинку')
    gallery = models.ForeignKey(Gallery, verbose_name='Галерея', blank=True, on_delete=models.CASCADE)

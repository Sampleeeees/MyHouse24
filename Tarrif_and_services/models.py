from django.db import models
from django.shortcuts import redirect


# Create your models here.
class Tarrif(models.Model):
    name_tarrif = models.CharField(max_length=250)
    description_tarrif = models.CharField(max_length=300)
    published = models.DateTimeField(blank=True, null=True)

class Measure(models.Model):
    name_measure = models.CharField(max_length=100)

    def __str__(self):
        return self.name_measure

class Service(models.Model):
    status_view = models.BooleanField()
    service = models.CharField(max_length=50)
    measure = models.ForeignKey(Measure, blank=True, null=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return redirect('setting_service')

    def __str__(self):
        return self.service

    def natural_key(self):
        return [self.measure.name_measure, self.service]


class ServiceforTariif(models.Model):
    service = models.ForeignKey(Service, verbose_name='Послуга', blank=True, on_delete=models.CASCADE)
    price = models.IntegerField(blank=True, null=True)
    tarrif = models.ForeignKey(Tarrif, verbose_name='Тариф', blank=True, on_delete=models.CASCADE)
    consum = models.IntegerField(blank=True, null=True)
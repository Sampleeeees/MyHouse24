from django.db import models

# Create your models here.
class Tarrif(models.Model):
    name_tarrif = models.CharField(max_length=250)
    description_tarrif = models.CharField(max_length=300)
    amount = models.FloatField()

class Measure(models.Model):
    name_measure = models.CharField(max_length=100)

class Service(models.Model):
    status_view = models.BooleanField()
    service = models.CharField(max_length=50)


class TarrifServices(models.Model):
    tarrif = models.ForeignKey(Tarrif, verbose_name='Тариф', blank=True, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, verbose_name='Послуги', blank=True, on_delete=models.CASCADE)
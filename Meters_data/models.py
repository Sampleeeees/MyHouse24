from django.db import models
from Tarrif_and_services.models import Service
from House.models import House, Section
from Appartament.models import Appartament
Choice_Status = {
    (None, 'Оберть...'),
    (1000, 'Нове'),
    (1000, 'Враховано'),
    (1000, 'Нульове')
}

# Create your models here.
class MetersData(models.Model):
    meters_data = models.CharField(max_length=50)
    date_published = models.DateField()
    status = models.CharField(max_length=50)
    meter = models.ForeignKey(Service, verbose_name='Лічильник', on_delete=models.CASCADE, blank=True, null=True)
    house = models.ForeignKey(House, verbose_name='Будинок', on_delete=models.CASCADE, blank=True, null=True)
    appartament = models.ForeignKey(Appartament, verbose_name='Квартира', on_delete=models.CASCADE, blank=True, null=True)
    section = models.ForeignKey(Section, verbose_name='Секція', on_delete=models.CASCADE, blank=True, null=True)
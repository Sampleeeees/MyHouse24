from django.db import models
from House.models import House, Section
from Appartament.models import Appartament
# Create your models here.
Choice_Status = {
    (None, 'Активний'),
    (10000, 'Неактивний'),
}

class PersonalBook(models.Model):
    status = models.CharField(max_length=50, choices=Choice_Status, blank=True)
    house = models.ForeignKey(House, verbose_name='Будинок', on_delete=models.CASCADE, blank=True)
    section = models.ForeignKey(Section, verbose_name='Секція', on_delete=models.CASCADE, blank=True)
    appartament = models.ForeignKey(Appartament, verbose_name='Квартира', on_delete=models.CASCADE, blank=True)
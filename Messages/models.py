from django.db import models
from House.models import House, Section, Floor
from Appartament.models import Appartament
# Create your models here.
class Message(models.Model):
    title_mess = models.CharField(max_length=80)
    date_send = models.DateTimeField(blank=True, null=True)
    user_send = models.CharField(max_length=120, blank=True, null=True)
    description_mess = models.CharField(max_length=350)
    house = models.ForeignKey(House, verbose_name='Будинок', on_delete=models.CASCADE, blank=True)
    section = models.ForeignKey(Section, verbose_name='Секція', on_delete=models.CASCADE, blank=True)
    floor = models.ForeignKey(Floor, verbose_name='Поверх', on_delete=models.CASCADE, blank=True)
    appartament = models.ForeignKey(Appartament, verbose_name='Квартира', on_delete=models.CASCADE, blank=True)
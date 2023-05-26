from django.db import models
from House.models import House, Floor, Section
from User.models import User
from Tarrif_and_services.models import Tarrif

# Create your models here.
class Appartament(models.Model):
    number_appartament = models.IntegerField()
    area = models.IntegerField()
    house = models.ForeignKey(House, verbose_name='Будинок', on_delete=models.CASCADE, blank=True)
    section = models.ForeignKey(Section, verbose_name='Секція', on_delete=models.CASCADE, blank=True)
    floor = models.ForeignKey(Floor, verbose_name='Поверх', on_delete=models.CASCADE, blank=True)
    owner = models.ForeignKey(User, verbose_name='Власник', on_delete=models.CASCADE, blank=True)
    tarrif = models.ForeignKey(Tarrif, verbose_name='Тариф', on_delete=models.CASCADE, blank=True)
    personal_book = models.ForeignKey('Personal_book.PersonalBook', related_name='PERI', verbose_name='ОсобистийРахунок', on_delete=models.CASCADE, blank=True, null=True)

    def natural_key(self):
        return self.number_appartament
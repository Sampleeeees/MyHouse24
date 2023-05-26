from django.db import models
from Tarrif_and_services.models import Tarrif
from Appartament.models import Appartament
from House.models import House, Section
from Personal_book.models import PersonalBook
# Create your models here.
Status_Pay = {
    ('Оплачена', 'Оплачена'),
    ('Частково оплачена', 'Частково оплачена'),
    ('Неоплачена', 'Неоплачена')
}

class Receipt(models.Model):
    confirm = models.BooleanField(null=True, default=False)
    price = models.CharField(max_length=50, blank=True, null=True)
    uid = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    status_pay = models.CharField(max_length=50, choices=Status_Pay, blank=True)
    tarrif = models.ForeignKey(Tarrif, verbose_name='Тариф', on_delete=models.CASCADE, blank=True)
    appartament = models.ForeignKey(Appartament, verbose_name='Квартира', on_delete=models.CASCADE, blank=True)
    house = models.ForeignKey(House, verbose_name='Будинок', on_delete=models.CASCADE, blank=True, null=True)
    section = models.ForeignKey(Section, verbose_name='Секція', on_delete=models.CASCADE, blank=True, null=True)
    personal_book = models.CharField(max_length=50, blank=True, null=True)

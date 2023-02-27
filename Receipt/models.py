from django.db import models
from Tarrif_and_services.models import Tarrif
from Appartament.models import Appartament
# Create your models here.
Status_Pay = {
    (None, 'Оберіть...'),
    (1000, 'Оплачена'),
    (2000, 'Частково оплачена'),
    (3000, 'Неоплачена ')
}

class Receipt(models.Model):
    confirm = models.BooleanField()
    date_created = models.DateField()
    status_pay = models.CharField(max_length=50, choices=Status_Pay, blank=True)
    tarrif = models.ForeignKey(Tarrif, verbose_name='Тариф', on_delete=models.CASCADE, blank=True)
    appartament = models.ForeignKey(Appartament, verbose_name='Квартира', on_delete=models.CASCADE, blank=True)
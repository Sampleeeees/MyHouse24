from django.db import models
from Tarrif_and_services.models import Tarrif
from Appartament.models import Appartament
# Create your models here.
Status_Pay = {
    ('Оплачена', 'Оплачена'),
    ('Частково оплачена', 'Частково оплачена'),
    ('Неоплачена', 'Неоплачена ')
}

Confirm_Choice = {
    ('Проведена', 'Проведена'),
    ('Не проведена', 'Не проведена'),
}
class Receipt(models.Model):
    confirm = models.CharField(choices=Confirm_Choice, max_length=50, blank=True, null=True)
    uid = models.CharField(max_length=50, blank=True, null=True)
    date_start = models.DateField(null=True)
    date_end = models.DateField(null=True)
    status_pay = models.CharField(max_length=50, choices=Status_Pay, blank=True)
    tarrif = models.ForeignKey(Tarrif, verbose_name='Тариф', on_delete=models.CASCADE, blank=True)
    appartament = models.ForeignKey(Appartament, verbose_name='Квартира', on_delete=models.CASCADE, blank=True)
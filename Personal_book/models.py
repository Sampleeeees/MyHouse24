from django.db import models
from House.models import House, Section
from Appartament.models import Appartament
from User.models import User
# Create your models here.
Choice_Status = {
    (None, 'Активний'),
    (10000, 'Неактивний'),
}

Residual_Status = {
    ('Є борг', 'Є борг'),
    ('Немає боргу', 'Немає боргу')
}

class PersonalBook(models.Model):
    status = models.CharField(max_length=50, choices=Choice_Status, blank=True)
    house = models.ForeignKey(House, verbose_name='Будинок', on_delete=models.CASCADE, blank=True)
    section = models.ForeignKey(Section, verbose_name='Секція', on_delete=models.CASCADE, blank=True)
    owner = models.ForeignKey(User, verbose_name='Власник', on_delete=models.CASCADE, blank=True, null=True)
    appartament = models.ForeignKey(Appartament, verbose_name='Квартира', on_delete=models.CASCADE, blank=True)
    residual = models.CharField(max_length=150, blank=True, null=True, choices=Residual_Status)
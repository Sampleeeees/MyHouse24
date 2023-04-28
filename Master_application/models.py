from django.db import models
from User.models import User, Role
from Appartament.models import Appartament



Type_Status = {
    ('Нове', 'Нове'),
    ('В роботі', 'В роботі'),
    ('Виконано', 'Виконано')
}

# Create your models here.
class MatsterApplication(models.Model):
    description_problem = models.CharField(max_length=500)
    comment = models.CharField(max_length=250)
    date_master = models.DateField(blank=True, null=True)
    time_master = models.TimeField(blank=True, null=True)
    typeMaster = models.ForeignKey(Role, blank=True, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=Type_Status, blank=True)
    name_master = models.ForeignKey(User, related_name='User_to_role', verbose_name='Працівники', blank=True, null=True, on_delete=models.CASCADE)
    appartament = models.ForeignKey(Appartament, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Квартира')
    ownerAppartament = models.ForeignKey(User, verbose_name='Володар квартири', blank=True, on_delete=models.CASCADE)


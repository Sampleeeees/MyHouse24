from django.db import models
from User.models import User

Type_Master = {
    (None, ''),
    (10, 'Сантехник'),
    (20, 'Електрик'),
    (30, 'Слюсар')
}

Type_Status = {
    (None, ''),
    (10, 'Нове'),
    (20, 'В роботі'),
    (30, 'Виконано')
}

# Create your models here.
class MatsterApplication(models.Model):
    description_problem = models.CharField(max_length=500)
    comment = models.CharField(max_length=250)
    typeMaster = models.CharField(max_length=50, choices=Type_Master, blank=True, null=True)
    status = models.CharField(max_length=50, choices=Type_Status, blank=True)
    name_master = models.CharField(max_length=50)
    ownerAppartament = models.ForeignKey(User, verbose_name='Володар квартири', blank=True, on_delete=models.CASCADE)


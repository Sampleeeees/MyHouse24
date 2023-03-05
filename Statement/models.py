from django.db import models
from User.models import User

# Create your models here.
class Statement(models.Model):
    amount = models.FloatField()
    status_perfom = models.BooleanField()
    comment = models.CharField(max_length=250)
    date_published = models.DateField()
    user_manager = models.ForeignKey(User, related_name='User_manager', verbose_name='Менеджер', blank=True, on_delete=models.CASCADE)
    ownerAppartemnt = models.ForeignKey(User, related_name='Owner_appartament', verbose_name='ВолодарКвартири', blank=True, on_delete=models.CASCADE)
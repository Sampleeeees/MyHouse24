from django.db import models
from User.models import User
from Personal_book.models import PersonalBook
from Articles_and_detail_payments.models import Article

# Create your models here.

Status_Choice = {
    ('Проведений', 'Проведений'),
    ('Не проведений', 'Не проведений')}

Type_choice = {
    ('Прихід', 'Прихід'),
    ('Розхід','Розхід')
}

class Statement(models.Model):
    uid = models.IntegerField(null=True)
    amount = models.FloatField()
    type = models.CharField(max_length=50, choices=Type_choice, null=True, blank=True)
    status = models.CharField(max_length=50, choices=Status_Choice, null=True, blank=True)
    status_perfom = models.BooleanField(null=True)
    comment = models.CharField(max_length=250)
    date_published = models.DateField()
    user_manager = models.ForeignKey(User, related_name='User_manager', verbose_name='Менеджер', blank=True, on_delete=models.CASCADE)
    ownerAppartemnt = models.ForeignKey(User, related_name='Owner_appartament', verbose_name='ВолодарКвартири', blank=True, on_delete=models.CASCADE, null=True)
    personal_book = models.ForeignKey(PersonalBook, related_name='PersonalBook', verbose_name='ОсобистийРахунок', blank=True, null=True, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='Article', verbose_name='Стаття ',blank=True, null=True, on_delete=models.CASCADE )

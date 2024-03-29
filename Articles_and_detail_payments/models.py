from django.db import models
from django.shortcuts import redirect

# Create your models here.

Type_Article = {
    ('Прихід', 'Прихід'),
    ('Розхід', 'Розхід')
}

class Article(models.Model):
    name_article = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=Type_Article, blank=True)

    def get_absolute_url(self):
        return redirect('articleList')




class PaymentDetail(models.Model):
    name_company = models.CharField(max_length=100)
    information = models.CharField(max_length=300)

    def get_absolute_url(self):
        return redirect('paymentUpdate')

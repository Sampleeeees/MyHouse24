from django.db import models

# Create your models here.

Type_Article = {
    (None, 'Прихід'),
    (1, 'Розхід')
}

class Article(models.Model):
    name_article = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=Type_Article, blank=True)

class PaymentDetail(models.Model):
    name_company = models.CharField(max_length=100)
    information = models.CharField(max_length=300)

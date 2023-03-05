from django.contrib import admin
from .models import Article, PaymentDetail
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_article', 'type')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_company')


admin.site.register(Article, ArticleAdmin)
admin.site.register(PaymentDetail, PaymentAdmin)
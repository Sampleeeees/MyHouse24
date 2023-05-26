from django.contrib import admin
from .models import Receipt
# Register your models here.

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'date', 'confirm', 'tarrif', 'appartament')

admin.site.register(Receipt, ReceiptAdmin)
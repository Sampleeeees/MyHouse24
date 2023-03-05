from django.contrib import admin
from .models import MatsterApplication
# Register your models here.

class MasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'typeMaster', 'status', 'name_master', 'ownerAppartament')

admin.site.register(MatsterApplication, MasterAdmin)

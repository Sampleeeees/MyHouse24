from django.contrib import admin
from .models import MetersData
# Register your models here.

class MetersDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'meters_data', 'date_published', 'status', 'meter')

admin.site.register(MetersData, MetersDataAdmin)

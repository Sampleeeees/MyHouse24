from django.contrib import admin
from .models import Tarrif, Service, Measure
# Register your models here.

class TarrifAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_tarrif')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'service')

class MeasureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_measure')


admin.site.register(Tarrif, TarrifAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Measure, MeasureAdmin)
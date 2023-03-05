from django.contrib import admin
from .models import Tarrif, TarrifServices, Service, Measure
# Register your models here.

class TarrifAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_tarrif', 'amount')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'service')

class MeasureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_measure')

class TarrifServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'tarrif', 'service')

admin.site.register(Tarrif, TarrifAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Measure, MeasureAdmin)
admin.site.register(TarrifServices, TarrifServicesAdmin)
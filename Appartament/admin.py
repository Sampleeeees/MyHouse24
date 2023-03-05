from django.contrib import admin
from .models import Appartament
# Register your models here.

class AppartamentAdmin(admin.ModelAdmin):
    list_display = ('id', 'number_appartament', 'area', 'house', 'section', 'floor', 'owner')

admin.site.register(Appartament, AppartamentAdmin)
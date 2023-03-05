from django.contrib import admin
from .models import PersonalBook
# Register your models here.

class PersonalBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'house', 'section', 'appartament')

admin.site.register(PersonalBook, PersonalBookAdmin)

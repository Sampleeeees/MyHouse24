from django.contrib import admin
from .models import House, Floor, Section
# Register your models here.


class FloorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_floor')

class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_section')

class HouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_home')

admin.site.register(Floor, FloorAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(House, HouseAdmin)
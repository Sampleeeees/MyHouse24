from django.contrib import admin
from .models import Role, User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'id')

class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(User, UserAdmin)
admin.site.register(Role, RoleAdmin)

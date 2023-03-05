from django.contrib import admin
from .models import Statement
# Register your models here.

class StatementAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_published', 'amount', 'user_manager')

admin.site.register(Statement, StatementAdmin)
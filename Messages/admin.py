from django.contrib import admin
from .models import Message
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_mess', 'house', 'floor', 'section', 'appartament')

admin.site.register(Message, MessageAdmin)
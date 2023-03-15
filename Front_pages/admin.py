from django.contrib import admin
from .models import AboutUs, GeneralPage, BlockAndServices, SeoBlock, Contacts, Document
# Register your models here.

class GeneralPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'block', 'seo')

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'gallery')


class SeoBlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_seo')

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'email', 'seo')

admin.site.register(GeneralPage, GeneralPageAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(SeoBlock, SeoBlockAdmin)
admin.site.register(BlockAndServices)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Document)

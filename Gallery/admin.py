from django.contrib import admin
from .models import Gallery, Image
# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'gallery')

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image, ImageAdmin)

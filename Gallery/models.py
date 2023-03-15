from django.db import models
# Create your models here.

class Gallery(models.Model):
    text = models.CharField(max_length=100)


class Image(models.Model):
    image = models.ImageField(upload_to='gallery/image/', blank=True, null=True)
    text = models.CharField(max_length=100, blank=True, null=True)
    gallery = models.ForeignKey(Gallery, verbose_name='Галерея', on_delete=models.CASCADE, blank=True)

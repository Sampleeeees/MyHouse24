from django.db import models
from django.urls import reverse

from Gallery.models import Gallery
# Create your models here.

class SeoBlock(models.Model):
    title_seo = models.CharField(max_length=50)
    description_seo = models.CharField(max_length=250)
    keywords_seo = models.CharField(max_length=80)

class BlockAndServices(models.Model):
    image = models.ImageField(upload_to='blockAndServices')
    title = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=250, blank=True)

class GeneralPage(models.Model):
    title = models.CharField(max_length=70)
    short_text = models.CharField(max_length=270)
    image1 = models.ImageField(upload_to='GeneralPage/image')
    image2 = models.ImageField(upload_to='GeneralPage/image')
    image3 = models.ImageField(upload_to='GeneralPage/image')
    block = models.ForeignKey(BlockAndServices, verbose_name='Блок', on_delete=models.CASCADE, blank=True, null=True)
    seo = models.ForeignKey(SeoBlock, verbose_name='СЕО Блок', on_delete=models.CASCADE, blank=True, null=True)

class AboutUs(models.Model):
    title = models.CharField(max_length=70)
    title_sec = models.CharField(max_length=70, blank=True)
    short_text = models.CharField(max_length=200)
    short_text_sec = models.CharField(max_length=200, blank=True)
    image_director = models.ImageField(upload_to='aboutUs/', blank=True, null=True)
    gallery = models.ForeignKey(Gallery, verbose_name='Галерея', on_delete=models.CASCADE, blank=True, null=True)
    seo = models.ForeignKey(SeoBlock, verbose_name='СЕО Блок', on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('aboutUs', kwargs={'pk': self.pk})

class Contacts(models.Model):
    title = models.CharField(max_length=50)
    short_text = models.CharField(max_length=50)
    link = models.URLField()
    fio = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField()
    code_card = models.CharField(max_length=50)
    seo = models.ForeignKey(SeoBlock, verbose_name='СЕО Блок', on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('contacts', kwargs={'pk': self.pk})

class Document(models.Model):
    document = models.FileField(upload_to='document/', blank=True)
    text = models.CharField(max_length=100, blank=True)
    page = models.ForeignKey(AboutUs, verbose_name='ПроНас', blank=True, null=True, on_delete=models.CASCADE)
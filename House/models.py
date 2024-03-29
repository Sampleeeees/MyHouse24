from django.db import models
from User.models import User
from Gallery.models import Gallery
# Create your models here.
class House(models.Model):
    name_home = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    image1 = models.ImageField(upload_to='house/image/', blank=True, null=True)
    image2 = models.ImageField(upload_to='house/image/', blank=True, null=True)
    image3 = models.ImageField(upload_to='house/image/', blank=True, null=True)
    image4 = models.ImageField(upload_to='house/image/', blank=True, null=True)
    image5 = models.ImageField(upload_to='house/image/', blank=True, null=True)
    staff = models.ManyToManyField(User, related_name='ПрацівникиУБудинку', blank=True, null=True)
    def __str__(self):
        return self.name_home

    def natural_key(self):
        return self.name_home

class Floor(models.Model):
    name_floor = models.CharField(max_length=100)
    house = models.ForeignKey(House, verbose_name='Будинок', blank=True, null=True, on_delete=models.CASCADE)


class Section(models.Model):
    name_section = models.CharField(max_length=100)
    house = models.ForeignKey(House, verbose_name='Будинок', blank=True, null=True, on_delete=models.CASCADE)

    def natural_key(self):
        return self.name_section

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(max_length=10)
    description = models.TextField(max_length=100,default='', blank=True)
    image = models.ImageField(upload_to='products/')
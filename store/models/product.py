from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=100,default='', blank=True)
    image = models.ImageField(upload_to='uploads/products/')


    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()
        
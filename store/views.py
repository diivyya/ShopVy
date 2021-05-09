from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product

def index(request):
    product = Product.get_all_products()
    return render(request, 'index.html', {'products': product})
    

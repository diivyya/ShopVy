from django.shortcuts import render
from django.views import View
from store.models.product import Product
from store.models.order import Order
from store.models.customer import Customer

class Orders(View):
    def get(self, request):
        return render(request,'orders.html')
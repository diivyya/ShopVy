from django.shortcuts import render
from django.views import View
from store.models.order import Order

class Orders(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer_id(customer)

        return render(request,'orders.html', {'orders':orders})
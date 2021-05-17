from django.shortcuts import render
from django.views import View
from store.models.order import Order
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

class Orders(View):

    @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer_id(customer)

        return render(request,'orders.html', {'orders':orders})
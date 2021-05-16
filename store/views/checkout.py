from django.shortcuts import redirect
from django.views import View
from store.models.product import Product
from store.models.order import Order
from store.models.customer import Customer

class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        for product in products:
            print(product)
            order = Order(customer = Customer(id=customer), product=product, price=product.price, quantity=cart.get(str(product.id)), address=address, phone=phone )
            order.placeOrder()
        request.session['cart'] = {}
        return redirect('homepage')
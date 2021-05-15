from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product
from store.models.category import Category

class Index(View):
    def get(self, request):
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_category_id(categoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories
        print('you are: ',request.session.get('email'))
        return render(request, 'index.html', data)
    
    def post(self, request):
        product_id = request.POST.get('product_id')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product_id)
            if quantity:
                cart[product_id] = quantity + 1
            else:
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = 1
        request.session['cart'] = cart
        print(cart)
        return redirect('homepage') 


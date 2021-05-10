from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

def index(request):
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
    return render(request, 'index.html', data)

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        errorMessage = None
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        repassword = postData.get('repassword')
        values = {
            'firstname':first_name,
            'lastname':last_name,
            'phone':phone,
            'email':email
        }
        if password == repassword:
            customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
            customer.register()
            return redirect('homepage')
        else:
            errorMessage = 'Both Passwords should match'
            formData = {
                'error': errorMessage,
                'values': values
            }
            return render(request, 'signup.html',formData)

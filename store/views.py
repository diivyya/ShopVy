from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
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
        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
        if password != repassword:
            errorMessage = 'Both Passwords should match'
        if customer.userExists():
            errorMessage = 'Email ID is already registered.. Try to Login'

        if errorMessage:
            formData = {
                'error': errorMessage,
                'values': values
            }
            return render(request, 'signup.html', formData)
        else:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        errorMessage = None
        email = request.POST.get('email')
        password = request.POST.get('password')
        values = {
            'email': email,
            'password': password
        }
        customer = Customer.get_customer_by_email(email)

        if customer:
            if check_password(password, customer.password):
                return redirect('homepage')
            else:
                errorMessage = 'Wrong Password!!'
        else:
            errorMessage = 'Email id is not registered'
        formData = {
            'values': values,
            'error': errorMessage
        }
        return render(request, 'login.html', formData)


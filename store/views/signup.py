from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from store.models.customer import Customer

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    def post(self, request):
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
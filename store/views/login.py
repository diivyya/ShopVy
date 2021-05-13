from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.customer import Customer

class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
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
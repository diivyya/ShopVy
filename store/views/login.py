from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.customer import Customer

class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')
        
    def post(self, request):
        return_url = request.GET.get('return_url')
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
                request.session['customer'] = customer.id
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
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


def logout(request):
    request.session.clear()
    return redirect('homepage')
from django.contrib import admin
from django.urls import path
from .views import home,login,signup,cart,checkout,orders
from .views.login import logout
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('',home.Index.as_view(), name='homepage'),
    path('signup',signup.Signup.as_view(), name="signup"),
    path('login', login.Login.as_view(), name="login"),
    path('logout',logout,name="logout"),
    path('cart',auth_middleware(cart.Cart.as_view()), name="cart"),
    path('checkout',checkout.Checkout.as_view(), name="checkout"),
    path('orders',orders.Orders.as_view(), name="orders")
]

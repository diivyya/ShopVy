from django.contrib import admin
from django.urls import path
from .views import home,login,signup
from .views.login import logout

urlpatterns = [
    path('',home.Index.as_view(), name='homepage'),
    path('signup',signup.Signup.as_view(), name="signup"),
    path('login', login.Login.as_view(), name="login"),
    path('logout',logout,name="logout")
]

"""
accounts
"""
from django.urls import path 
from .views import loginview,signupview


app_name="accounts"

urlpatterns = [
    path('',loginview,name="login"),
    path('signup/',signupview,name="signup"),
]
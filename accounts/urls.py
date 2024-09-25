"""
accounts
"""
from django.urls import path 
from .views import loginview


app_name="accounts"

urlpatterns = [
    path('',loginview),
]
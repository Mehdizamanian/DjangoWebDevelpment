"""
accounts
"""
from django.urls import path 
from .views import login_view,signupview,logout_view


app_name="accounts"

urlpatterns = [
    path('login/',login_view,name="login"),
    path('logout/',logout_view,name="logout"),
    path('signup/',signupview,name="signup"),
]
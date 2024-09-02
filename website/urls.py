
"""   URL website  """

from django.urls import path 
from .views import home ,about,contact
app_name='website'

urlpatterns = [
    path('',home,name="home"),
    path('aboutus/',about,name="about"),
    path('contactus/',contact,name="contact"),
    
]

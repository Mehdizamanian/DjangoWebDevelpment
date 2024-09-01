
"""   URL website  """

from django.urls import path 
from .views import home ,about,contact,blog,post_details
app_name='website'

urlpatterns = [
    path('',home,name="home"),
    path('aboutus/',about,name="about"),
    path('contactus/',contact,name="contact"),
    path('blog/',blog,name="blog"),
    path('post-details/',post_details,name="post_details"),
]

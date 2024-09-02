
"""
URL Blogs
"""


from django.urls import path 
from .views import blog , post_details
app_name="blogs"

urlpatterns = [
    path('posts/',blog , name="blog"),
    path('post-details/',post_details , name="post-details"),

]

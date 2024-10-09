
"""
all urls begins with blogs/....
"""


from django.urls import path 
from .views import blog , post_details
app_name="blogs"

urlpatterns = [
    path('',blog , name="blog"),
    path('posts/post-detail/<int:num>/',post_details , name="post-details"),
    path('category/<cat>/',blog ,name="category"),
    path('author/<auth>/',blog ,name="author"),

]


"""
all urls begins with blogs/....
"""


from django.urls import path 
from .views import blog , post_details,PostList,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
app_name="blogs"

urlpatterns = [
    path('',blog , name="blog"),
    path('posts/post-detail/<int:num>/',post_details , name="post-details"),
    path('category/<cat>/',blog ,name="category"),
    path('author/<auth>/',blog ,name="author"),
    #admin dashboard
    path('dashboard/',PostList.as_view(),name="dashboard"),
    path('dashboard/detail/<int:pk>/',PostDetailView.as_view(),name="dashboard-detail"),
    path('dashboard/create/',PostCreateView.as_view(),name="create"),
    path('dashboard/edit/<int:pk>',PostUpdateView.as_view(),name="edite"),
    path('dashboard/delete/<int:pk>/',PostDeleteView.as_view(),name="delete"),
]

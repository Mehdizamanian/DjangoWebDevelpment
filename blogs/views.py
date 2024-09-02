from django.shortcuts import render ,HttpResponse
from .models import Post


def blog(request):
  posts=Post.objects.all()
  context={'posts':posts}
  return render(request,'blogs/blog.html', context)


def post_details(request):
  return render(request,'blogs/post-details.html')

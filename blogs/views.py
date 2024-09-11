from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from .models import Post


def blog(request):
  posts=Post.objects.filter(active=True)
  context={'posts':posts}
  return render(request,'blogs/blog.html', context)


def post_details(request , num):
  try:
      post=Post.objects.get(id=num)
      context={'post':post}

  except post.DoesNotExsit:
     return HttpResponse('<h1>404 Error </h1>')

  
  return render(request,'blogs/post-details.html',context)

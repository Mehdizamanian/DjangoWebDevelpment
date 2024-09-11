from django.shortcuts import render ,get_object_or_404
from .models import Post


def blog(request):
  posts=Post.objects.filter(active=True)
  context={'posts':posts}
  return render(request,'blogs/blog.html', context)


def post_details(request , num):
  post=get_object_or_404(Post,id=num)
  context={'post':post}
  return render(request,'blogs/post-details.html',context)

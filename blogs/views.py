from django.shortcuts import render ,get_object_or_404,redirect
from .models import Post , Comment
from .forms import CommentForm
from django.db.models import Q


def blog(request,**kwargs):
  posts=Post.objects.filter(active=True)

  if kwargs.get('cat'):
    posts=posts.filter(category__title=kwargs['cat'])
    
  if kwargs.get('auth'):
   posts=posts.filter(author__username=kwargs['auth'])


  search=request.GET.get('q')
  if search:
     posts=posts.filter(Q(title__icontains=search) | Q(description__icontains=search))

  context={'posts':posts}
  return render(request,'blogs/blog.html', context)


def post_details(request , num):
  post=get_object_or_404(Post,id=num)
  comments=Comment.objects.filter(active=True,post=post)

  form=CommentForm()
  
  if request.method=="POST":
    form=CommentForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/')

  context={'post':post,'comments':comments,'form':form}
  return render(request,'blogs/post-details.html',context)

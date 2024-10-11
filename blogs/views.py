from django.db.models.query import QuerySet
from django.shortcuts import render ,get_object_or_404,redirect
from .models import Post , Comment
from .forms import CommentForm
from django.db.models import Q
from django.contrib import messages

from django.views.generic import ListView , DetailView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin



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
      messages.success(request, "your comment added and would be published soon ... ")
      return redirect('/')

  context={'post':post,'comments':comments,'form':form}
  return render(request,'blogs/post-details.html',context)










# admin Dashbord 

class PostList(UserPassesTestMixin,ListView):
  model=Post
  template_name='blogs/dashboard.html'
  context_object_name='posts'

  def test_func(self):
      return self.request.user.is_superuser

  # def get_queryset to get filter and search


class PostDetailView(UserPassesTestMixin,DetailView):
  model=Post
  template_name='blogs/dashboard-detail.html'
  context_object_name='post'

  def test_func(self):
      return self.request.user.is_superuser



class PostCreateView(UserPassesTestMixin,SuccessMessageMixin,CreateView):
  model=Post
  template_name='blogs/dashboard-form.html'
  fields='__all__'
  success_url=reverse_lazy('blogs:dashboard')
  success_message = "new Post created "

  def test_func(self):
      return self.request.user.is_superuser
  


class PostUpdateView(UserPassesTestMixin,SuccessMessageMixin,UpdateView):
  model=Post
  template_name='blogs/dashboard-form.html'
  fields='__all__'
  success_url=reverse_lazy('blogs:dashboard')
  success_message = "one post updated successfully"

  def test_func(self):
      return self.request.user.is_superuser



class PostDeleteView(UserPassesTestMixin,SuccessMessageMixin,DeleteView):
  model=Post
  template_name='blogs/dashboard-delete.html'
  fields='__all__'
  success_url=reverse_lazy('blogs:dashboard')
  success_message = "one post Deleted successfully"

  def test_func(self):
      return self.request.user.is_superuser
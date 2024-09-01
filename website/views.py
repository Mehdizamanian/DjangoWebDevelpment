from django.shortcuts import render , HttpResponse


def home(request):
  return render(request,'website/index.html')

def about(request):
  return render(request,'website/about.html')

def contact(request):
  return render(request,'website/contact.html')


def blog(request):
  return render(request,'website/blog.html')


def post_details(request):
  return render(request,'website/post-details.html')



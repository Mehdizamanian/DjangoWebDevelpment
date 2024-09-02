from django.shortcuts import render ,HttpResponse



def blog(request):
  return render(request,'blogs/blog.html')


def post_details(request):
  return render(request,'blogs/post-details.html')

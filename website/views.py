from django.shortcuts import render , HttpResponse,redirect
from .models import Contact
from .forms import ContactForm


def home(request):
  return render(request,'website/index.html')

def about(request):
  return render(request,'website/about.html')

def contact(request):
  if request.method=="POST":
    form=form=ContactForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/')
  form=ContactForm()
  return render(request,'website/contact.html',{'form':form})


# def post_details(request):
#   return render(request,'website/post-details.html')



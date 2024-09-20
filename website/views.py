from django.shortcuts import render , HttpResponse,redirect
from .models import Contact
from .forms import ContactForm


def home(request):
  return render(request,'website/index.html')

def about(request):
  return render(request,'website/about.html')


def contact(request):

  if request.method=="POST":
    form=ContactForm(request.POST)
    if form.is_valid():
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        subject=form.cleaned_data['subject']
        message=form.cleaned_data['message']
        c=Contact()
        c.name=name
        c.email=email
        c.subject=subject
        c.message=message
        c.save()
        return redirect('/')

  
  # if request.method=='POST':
  #   form=ContactForm(request.POST)
  #   if form.is_valid():
  #     form.save()
  #     redirect('/') 

  # form=ContactForm()
    
  return render(request,'website/contact.html',)







# def post_details(request):
#   return render(request,'website/post-details.html')



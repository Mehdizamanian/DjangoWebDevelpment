from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def loginview(request):
  return render(request,'accounts/login.html')

# Create your views here.
def signupview(request):
  if request.method=='POST':
    form=UserCreationForm(request.POST)
    if form.is_valid():
      # messages.success(request,'your account created successfully to log in below')
      form.save()
      return redirect("blogs:blog")
  else:    
    form=UserCreationForm
  return render(request,'accounts/signup.html',{'form':form})
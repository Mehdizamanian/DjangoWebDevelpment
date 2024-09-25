from django.shortcuts import render


def loginview(request):
  return render(request,'accounts/registration.html')

# Create your views here.

from django.db import models


class Contact(models.Model):
  name=models.CharField(max_length=60)
  email=models.EmailField(max_length=254)
  subject=models.CharField(max_length=254)
  message=models.TextField()

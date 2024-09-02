from django.db import models


class Post(models.Model):
  title=models.CharField(max_length=254)
  description=models.TextField()
  active=models.BooleanField(default=False)
  author=models.CharField(max_length=70)
  updated_time=models.DateField(auto_now=True)
  created_time=models.DateField(auto_now_add=True)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name="پست  "
    verbose_name_plural="پست ها "


  



from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager

User=get_user_model()

class Post(models.Model):
  title=models.CharField(max_length=254)
  description=models.TextField()
  active=models.BooleanField(default=False)
  updated_time=models.DateField(auto_now=True)
  created_time=models.DateField(auto_now_add=True)
  # rel
  author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
  image=models.ImageField(upload_to='blogs/images/',default="blogs/images/1.png")
  category=models.ManyToManyField("Category")
  breif_description=models.CharField(max_length=80,null=True,blank=True)
  # endrel
  tags = TaggableManager()


  def __str__(self):
    return self.title

  class Meta:
    verbose_name="پست  "
    verbose_name_plural="پست ها "
    ordering=['created_time']


class Category(models.Model):
  title=models.CharField(max_length=80)

  def __str__(self):
    return self.title
  



class Comment(models.Model):
  post=models.ForeignKey(Post,on_delete=models.CASCADE)
  name=models.CharField(max_length=90)
  email=models.EmailField(max_length=150)
  subject=models.CharField(max_length=254)
  message=models.TextField()
  created_time=models.DateTimeField(auto_now_add=True)
  active=models.BooleanField(default=False)

  def __str__(self):
    return self.name

  class Meta:
    ordering=['-created_time',]


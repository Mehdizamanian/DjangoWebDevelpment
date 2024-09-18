
from django import template
from blogs.models import Post,Category
from persiantools.jdatetime import JalaliDate
from taggit.models import Tag

register=template.Library()


@register.simple_tag
def mycustom_tag():
  return "this is just my custom template tags :) "


@register.filter
def upper(value):
  return value.upper()


@register.inclusion_tag('blogs/includes/blog-recent.html')
def recent_post():
  posts=Post.objects.filter(active=True).order_by('-created_time')[:2]
  return {'posts':posts}


@register.filter
def jalilidate(value):
  return JalaliDate(value).strftime("%Y/%m/%d")

# showing just name category
# @register.inclusion_tag('blogs/includes/blog-categories.html')
# def categories():
#   categories=Category.objects.all()
#   return {'categories':categories}

@register.inclusion_tag('blogs/includes/blog-categories.html')
def categories():
  categories=Category.objects.all() 
  posts=Post.objects.filter(active=True)
  categories_count={}

  for cat in categories:
    categories_count[cat]=posts.filter(category__title=cat).count()

  return {'categories_count':categories_count}



@register.inclusion_tag('blogs/includes/blog-tags.html')
def tag_post():
  tags=Tag.objects.all()
  return {'tags':tags}



from django import template
from blogs.models import Post
from persiantools.jdatetime import JalaliDate


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

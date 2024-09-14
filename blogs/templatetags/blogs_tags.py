
from django import template

register=template.Library()


@register.simple_tag
def mycustom_tag():
  return "this is just my custom template tags :) "
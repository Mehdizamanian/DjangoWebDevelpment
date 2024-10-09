from django.contrib import admin
from .models import Post , Category , Comment
from django_summernote.admin import SummernoteModelAdmin


class CommentAdminInline(admin.StackedInline):
  model=Comment
  fields=['name','email','message','active']
  extra=0


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
  list_display=['id','title','active']
  list_filter=['active']
  search_fields=('title','description',)
  date_hierarchy='created_time'
  list_display_links=['id','title']
  inlines=[CommentAdminInline]
  summernote_fields = ('description',)



class CategoryAdmin(admin.ModelAdmin):
  list_display=['title']
  search_fields=('title',)

admin.site.register(Category,CategoryAdmin)




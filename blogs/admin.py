from django.contrib import admin

from .models import Post , Category , Comment


class CommentAdminInline(admin.TabularInline):
  model=Comment
  fields=['name','email','message','active']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display=['id','title','active']
  list_filter=['active']
  search_fields=('title','description',)
  date_hierarchy='created_time'
  list_display_links=['id','title']
  inlines=[CommentAdminInline]



class CategoryAdmin(admin.ModelAdmin):
  list_display=['title']
  search_fields=('title',)

admin.site.register(Category,CategoryAdmin)




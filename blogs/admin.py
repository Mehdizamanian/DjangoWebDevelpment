from django.contrib import admin

from .models import Post , Category , Comment


class PostAdmin(admin.ModelAdmin):
  list_display=['id','title','active']
  list_filter=['active']
  search_fields=('title','description',)
  date_hierarchy='created_time'
  list_display_links=['id','title']

admin.site.register(Post,PostAdmin)



class CategoryAdmin(admin.ModelAdmin):
  list_display=['title']
  search_fields=('title',)

admin.site.register(Category,CategoryAdmin)



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display=['post','name','email','active']

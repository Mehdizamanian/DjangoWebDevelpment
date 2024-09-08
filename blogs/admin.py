from django.contrib import admin

from .models import Post , Category


class PostAdmin(admin.ModelAdmin):
  list_display=['id','title','author','active']
  list_filter=['active']
  search_fields=('title','description',)
  date_hierarchy='created_time'
  list_display_links=['id','title']

admin.site.register(Post,PostAdmin)



class CategoryAdmin(admin.ModelAdmin):
  list_display=['title']
  search_fields=('title',)

admin.site.register(Post,PostAdmin)

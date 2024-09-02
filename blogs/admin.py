from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
  list_display=['id','title','author','active']
  list_filter=['active']
  search_fields=('title','description',)
  date_hierarchy='created_time'
  list_display_links=['id','title']

admin.site.register(Post,PostAdmin)



from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display=['id','name','email']
  search_fields=('name','email','subject','message',)

# Register your models here.

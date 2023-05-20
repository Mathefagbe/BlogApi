from django.contrib import admin
from .models import BlogPost



class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=['title','status','author']


# Register your models here.
admin.site.register(BlogPost,BlogPostAdmin)
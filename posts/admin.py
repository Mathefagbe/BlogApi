from django.contrib import admin
from .models import BlogPost
from django.db import models
from tinymce.widgets import TinyMCE



class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=['title','status','author']
    formfield_overrides={
        models.TextField:{
            'widget':TinyMCE()
        }
    }


# Register your models here.
admin.site.register(BlogPost,BlogPostAdmin)
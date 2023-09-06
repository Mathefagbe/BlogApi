from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify
import secrets


# Create your models here.


def custom_slug(*args):
    hexformate=secrets.token_hex(7)
    origin_slug=slugify(args)
    unique_slug=origin_slug
    return f'{unique_slug}-{hexformate}'




#creating a manager that returns only post that has been published
class PusblisedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=BlogPost.Status.Published)

#creating a blogpost
class BlogPost(models.Model):
    class Status(models.TextChoices):
        Published='PB','Pusblished'
        Draft='DF','Draft'
    title=models.CharField(max_length=250)
    body=models.TextField()
    image=models.ImageField(upload_to='blogimage/%Y/%m/',blank=True)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='author')
    status=models.CharField(choices=Status.choices,default=Status.Draft,max_length=2)
    slug=models.SlugField(max_length=250)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField(default=timezone.now)

    #objects manager to query all
    objects=models.Manager()

    #published manage
    published=PusblisedManager()


    class Meta:
        ordering=['-published_date','-created_date']



    def __str__(self) -> str:
        return self.title

    def save(self,*args,**kwargs):
        self.slug=custom_slug(self.title)
        return super().save(*args,**kwargs)
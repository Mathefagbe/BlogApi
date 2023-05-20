from django.db import models
from posts.models import BlogPost
from django.conf import settings


# Create your models here.


class Likes(models.Model):
    post=models.ForeignKey(BlogPost,on_delete=models.CASCADE,related_name='liked_post')
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user_post_liked')
    dateliked=models.DateTimeField(auto_now_add=True)



    class Meta:
        indexes = [
        models.Index(fields=['user','post','id']),
            ]
        ordering = ['-dateliked']
        verbose_name_plural='Likes'

    def __str__(self) -> str:
        return f"{self.user} liked {self.post}"
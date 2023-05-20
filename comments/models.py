from django.db import models
from posts.models import BlogPost
from django.conf import settings

# Create your models here.

class Comment(models.Model):
    post=models.ForeignKey(BlogPost,on_delete=models.CASCADE, related_name='comment')
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='author_comment')
    comment=models.TextField()
    comment_date=models.DateTimeField(auto_now=True)


    class Meta:
        ordering=['-comment_date']



    def __str__(self) -> str:
        return self.comment
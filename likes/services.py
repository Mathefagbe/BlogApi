from .models import Likes
from django.shortcuts import get_object_or_404
from posts.models import BlogPost
from rest_framework.response import Response
from rest_framework import status

def like_post(self):
        post_id=self.kwargs['slug']
        post=get_object_or_404(BlogPost,slug=post_id)
        if post.like.filter(id=self.request.user.id).exists():
            Likes.objects.filter(post=post,user=self.request.user).delete()
            context={
                'status':'unlike'
            }
            return Response(context,status=status.HTTP_201_CREATED)
        else:
            Likes.objects.create(post=post,user=self.request.user)
            context={
                'status':'liked'
            }
            return Response(context,status=status.HTTP_201_CREATED)  
         
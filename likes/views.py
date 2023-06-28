from rest_framework.generics import  CreateAPIView
from .serializers import LikedPostSerializer
from .models import Likes
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from posts.models import BlogPost
from .services import  like_post
# from .selector import get_like


class LikedPostView(CreateAPIView):
    serializer_class=LikedPostSerializer
    permission_classes=[IsAuthenticated,]

    def post(self, request, *args, **kwargs):
        return like_post(self)
        
            
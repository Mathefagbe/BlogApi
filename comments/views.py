from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404,get_list_or_404
from .serializers import CommentPostSerializer
from rest_framework.generics import ListAPIView,CreateAPIView
from posts.models import BlogPost
from .models import Comment
from drf_yasg.utils import swagger_auto_schema


class CommentListApi(ListAPIView):
    serializer_class=CommentPostSerializer
    permission_classes=[IsAuthenticated]
    

    @swagger_auto_schema(
    operation_summary="list all comments",
    operation_description="This returns comments based on the post"
)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        post=get_object_or_404(BlogPost,slug=self.kwargs['slug'])
        comment=Comment.objects.select_related('post','author').filter(post=post).all()
        return comment

class CommentCreateApi(CreateAPIView):
    serializer_class=CommentPostSerializer
    permission_classes=[IsAuthenticated]
    lookup_field='slug'

    @swagger_auto_schema(
    operation_summary="create a comment",
    operation_description="This create a comment for the post"
)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    

    def get_serializer_context(self):
        post=get_object_or_404(BlogPost,slug=self.kwargs[self.lookup_field])
        return {'post':post,'user':self.request.user,'request':self.request}
    

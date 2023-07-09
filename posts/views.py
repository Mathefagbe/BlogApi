from rest_framework.generics import (ListAPIView,RetrieveAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     ListCreateAPIView)
from .serializers import BlogDetailSerializer,PostListSerializer
from rest_framework.permissions import IsAuthenticated
from .models import BlogPost
from .selector import get_post_status
from rest_framework import filters
from .pagination import DefaultPagination
from drf_yasg.utils import swagger_auto_schema



class BlogPostListView(ListAPIView):
    serializer_class=PostListSerializer
    permission_classes=[IsAuthenticated]
    filter_backends=[filters.SearchFilter]
    search_fields = ['title']
    
    # pagination_class=DefaultPagination
    
    def get_queryset(self):
        return BlogPost.objects.select_related('author').all()
    
class BlogPostDetailView(RetrieveAPIView):
    serializer_class=BlogDetailSerializer
    permission_classes=[IsAuthenticated]
    lookup_field='slug'

    def get_queryset(self):
        return BlogPost.objects.select_related('author',).prefetch_related('comment').all()
    @swagger_auto_schema(
    operation_summary="Get a blog post based on the slug",
    operation_description="This returns  a blog post"
)
    def get(self, request, *args, **kwargs):
        return get_post_status(self)
     
    def get_serializer_context(self):
        return {'request':self.request,'slug':self.kwargs[self.lookup_field]}
    

class AuthorBlogPostView(ListCreateAPIView):
    serializer_class=PostListSerializer
    permission_classes=[IsAuthenticated]
    # pagination_class=DefaultPagination

    def get_serializer_context(self):
        return {'user':self.request.user,'request':self.request}
    
    def get_queryset(self):
        userpost=BlogPost.objects.filter(author=self.request.user).all()
        return userpost
    @swagger_auto_schema(
    operation_summary="List all post of the login user",
    operation_description="This returns  a List of all the login user post"
)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
 
class AuthorBlogPostUpdateRetrieveDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class=PostListSerializer
    permission_classes=[IsAuthenticated]
    lookup_field='slug'

    def get_serializer_context(self):
        return {'user':self.request.user,'request':self.request}
  
    def get_queryset(self):
        userpost=BlogPost.objects.filter(author=self.request.user).all()
        return userpost
    

class BloggerProfilePostListView(ListAPIView):
    serializer_class=PostListSerializer
    permission_classes=[IsAuthenticated]
    # pagination_class=DefaultPagination

    def get_queryset(self):
        bloggerPost=BlogPost.objects.filter(author=self.kwargs['id']).all()
        return bloggerPost

    @swagger_auto_schema(
    operation_summary="List all post a user based on the user id",
    operation_description="This returns a list of a particular user post"
)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
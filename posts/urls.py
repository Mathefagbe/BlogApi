from django.contrib import admin
from django.urls import path
from .views import (
    BlogPostListView,
    BlogPostDetailView,
    AuthorBlogPostView,
    AuthorBlogPostUpdateRetrieveDeleteView,
    BloggerProfilePostListView
    )

urlpatterns = [
    path('posts/',BlogPostListView.as_view(),name='posts_list'),
    path('post/<slug>/',BlogPostDetailView.as_view(),name='post_detail'),
    path('posts/user/',AuthorBlogPostView.as_view(),name='user_post_list'),
    path('post/user/<slug>/',AuthorBlogPostUpdateRetrieveDeleteView.as_view(),name='user_update_edit'), 
    path('posts/blogger/<id>/',BloggerProfilePostListView.as_view(),name='blogger_post_list'),        
]
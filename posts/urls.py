from django.contrib import admin
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    UserPostView,
    UserPostUpdateRetrieveDeleteView,
    AuthorPostListView
    )

urlpatterns = [
    path('posts/',PostListView.as_view(),name='posts_list'),
    path('post/<slug>/',PostDetailView.as_view(),name='post_detail'),
    path('posts/user/',UserPostView.as_view(),name='user_post_list'),
    path('post/user/<slug>/',UserPostUpdateRetrieveDeleteView.as_view(),name='user_update_edit'), 
    path('posts/author/<id>/',AuthorPostListView.as_view(),name='blogger_post_list'),        
]
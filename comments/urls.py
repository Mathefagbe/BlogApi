from django.urls import path
from .views import CommentCreateApi,CommentListApi

urlpatterns = [
    path('comment/<slug>/create/' ,CommentCreateApi.as_view(),name='comment_create'),
    path('comment/<slug>/' ,CommentListApi.as_view(),name='comment_list'),
]
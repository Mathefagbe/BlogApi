from django.contrib import admin
from django.urls import path
from .views import UsersProfileView,SingleAuthorProfileView

urlpatterns = [
    path('profile/',UsersProfileView.as_view(),name='userprofile'),
    path('profile/<id>',SingleAuthorProfileView.as_view(),name='author_retrive')
]
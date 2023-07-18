from django.urls import path
from .views import UserProfileView,AuthorProfileView

urlpatterns = [
    path('profile/',UserProfileView.as_view(),name='userprofile'),
    path('profile/<id>',AuthorProfileView.as_view(),name='author_retrive')
]
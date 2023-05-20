from django.urls import path
from .views import LikedPostView

urlpatterns = [
    path('post/<slug>/likes/',LikedPostView.as_view(),name='like'), 
]
from django.urls import path
from .views import FollowingView,FollowersListView,FollowingCreateView

urlpatterns = [
    path('users/following/',FollowingCreateView.as_view(),name='following_create'),
    path('users/following/<id>',FollowingView.as_view(),name='following_list'),
    path('users/follower/<id>',FollowersListView.as_view(),name='follower_list'),  
]
from django.urls import path
from .views import FollowingView,FollowersListView,FollowingCreateView

urlpatterns = [
    path('following/create/',FollowingCreateView.as_view(),name='following_create'),
    path('followings/<id>/',FollowingView.as_view(),name='following_list'),
    path('followers/<id>/',FollowersListView.as_view(),name='follower_list'),  
]
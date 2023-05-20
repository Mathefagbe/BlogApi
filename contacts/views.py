from rest_framework.generics import ListAPIView,CreateAPIView
from .serializers import (FollowingSerializer,
                          FollowingListSerializer,
                          FollowerListSerializer)
from rest_framework.permissions import IsAuthenticated
from .models import Contact
from .services import post_with_follow_status
from .selector import get_following_list,get_follower_list
from .pagination import DefaultPagination
from drf_yasg.utils import swagger_auto_schema
# from rest_framework import filters

# Create your views here.


class FollowingView(ListAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=FollowingListSerializer
    pagination_class=DefaultPagination

    def get_queryset(self):
        return Contact.objects.select_related('user_to','user_from')\
            .filter(user_from=self.kwargs['id']).all()
    @swagger_auto_schema(
    operation_summary="list all following",
    operation_description="This returns a list of following"
)
    def get(self, request, *args, **kwargs):
        return get_following_list(self)
    


class FollowersListView(ListAPIView):
    serializer_class=FollowerListSerializer
    permission_classes=[IsAuthenticated]
    pagination_class=DefaultPagination

    def get_queryset(self):
        return Contact.objects.select_related('user_to','user_from')\
            .filter(user_to=self.kwargs['id']).all()
    
    @swagger_auto_schema(
    operation_summary="list all followers",
    operation_description="This returns a list of followers"
)
    def get(self, request, *args, **kwargs):
        return get_follower_list(self)
        
        
        

class FollowingCreateView(CreateAPIView):
    permission_classes=[IsAuthenticated] 
    serializer_class= FollowingSerializer
    
    @swagger_auto_schema(
    operation_summary="create following with other users",
    operation_description="This create a following relationship with other users"
)
    def post(self, request, *args, **kwargs):
        return post_with_follow_status(self,request)
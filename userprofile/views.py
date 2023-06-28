from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView,RetrieveAPIView
from .serializers import UserProfileSerializer,SingleUserSerializer
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
# Create your views here.


class UsersProfileView(RetrieveUpdateAPIView):
    serializer_class=UserProfileSerializer
    permission_classes=[IsAuthenticated]

    def get_object(self):
        obj = get_object_or_404(UserProfile, user=self.request.user)
        self.check_object_permissions(self.request, obj)
        return obj

    @swagger_auto_schema(
    operation_summary="Get the login user profile",
    operation_description="This returns the profile of the login user"
)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(
    operation_summary="update the login user profile",
    operation_description="This returns the updated profile of the login user"
)
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
 
    def get_serializer_context(self):
        return {'request':self.request,'user':self.request.user}




class SingleAuthorProfileView(RetrieveAPIView):
    queryset=UserProfile.objects.all()
    serializer_class=SingleUserSerializer
    permission_classes=[IsAuthenticated]
    lookup_field='id'

    @swagger_auto_schema(
    operation_summary="Get a single user",
    operation_description="This returns a single user from a list of users"
)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_serializer_context(self):
        return {'request':self.request,'user_id': self.kwargs[self.lookup_field]}
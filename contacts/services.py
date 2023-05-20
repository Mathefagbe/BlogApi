from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import Contact
from rest_framework import status
from rest_framework.response import Response


def post_with_follow_status(self,request):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    User=get_user_model()
    user_to=serializer.validated_data.get('user_to',None)
    current_user=get_object_or_404(User,username=self.request.user)
    followed_user=get_object_or_404(User,id=user_to.id)
    if current_user.following.filter(id=followed_user.id).exists():
        Contact.objects.filter(user_to=followed_user, user_from=current_user).delete()
        headers = self.get_success_headers(serializer.data)
        context={
                 "status":"Unfollow"
             }
        return Response(context,status=status.HTTP_201_CREATED,headers=headers)
    else:
        Contact.objects.create(user_from=self.request.user,user_to=followed_user)
        headers = self.get_success_headers(serializer.data)
        context={
                 "status":"followed"
             }
        return Response(context,status=status.HTTP_201_CREATED,headers=headers)
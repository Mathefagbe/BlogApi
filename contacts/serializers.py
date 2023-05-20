from rest_framework import serializers
from .models import Contact
from account.serializers import CustomUserSerializer


# A serializer that is use to follow other users
class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=['user_to']


# A serializer to list the number of person you following
class FollowingListSerializer(serializers.ModelSerializer):
    user_to=CustomUserSerializer()
   
    class Meta:
        model=Contact
        fields=['user_to']


# A serializer to list the number of person following you
class FollowerListSerializer(serializers.ModelSerializer):
    user_from=CustomUserSerializer()
    class Meta:
        model=Contact
        fields=['user_from']






  
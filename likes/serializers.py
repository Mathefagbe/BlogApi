from rest_framework import serializers 
from .models import Likes
from account.serializers import CustomUserSerializer

 
class LikedPostSerializer(serializers.ModelSerializer):
    user=CustomUserSerializer(read_only=True)
    class Meta:
        model=Likes
        fields=['user']
        extra_kwargs={
            'dateliked':{'read_only':True,},
            'post':{'read_only':True,}
        }






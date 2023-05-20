from rest_framework import serializers
from .models import UserProfile
from contacts.models import Contact

class UserSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    username=serializers.CharField()
    email=serializers.EmailField()
    first_name=serializers.CharField()
    

class UserProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    followers=serializers.SerializerMethodField(read_only=True)
    following=serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        fields=['image','bio','user', 'followers','following']
        model=UserProfile

   
    def get_followers(self,obj):
        return Contact.objects.select_related('user_to','user_from')\
            .filter(user_to=self.context['user']).count()
    
    def get_following(self,obj):
        return Contact.objects.select_related('user_to','user_from')\
            .filter(user_from=self.context['user']).count()
    


class SingleUserSerializer(UserProfileSerializer):
   
    def get_followers(self,obj):
        return Contact.objects.select_related('user_to','user_from')\
            .filter(user_to=self.context['user_id']).count()
    
    def get_following(self,obj):
        return Contact.objects.select_related('user_to','user_from')\
            .filter(user_from=self.context['user_id']).count()
    

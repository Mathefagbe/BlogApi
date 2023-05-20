from django.contrib.auth import authenticate
from rest_framework import serializers

from contacts.models import Contact
from .models import CustomUser
from knox.serializers import UserSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.serializers import AuthTokenSerializer


class UserImageProfile(serializers.Serializer):
    image=serializers.ImageField()
    bio=serializers.CharField()
    

class CustomUserSerializer(UserSerializer):
    userprofile=UserImageProfile()
    class Meta:
        model=CustomUser
        fields=['id','username','email','first_name','userprofile','last_login']


# **********************************
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['username','first_name','last_name','email','password','confirm_password']
        extra_kwargs={
            'username':{'help_text':''},
            'password':{'write_only':True,},
            'confirm_password':{'write_only':True,},
        }

    def validate(self, attrs):
        attrs=super().validate(attrs)
        if attrs['password']!=attrs['confirm_password']:
            raise serializers.ValidationError({'error':"Password doesn't match"})
        if CustomUser.objects.filter(email__iexact=attrs['email']):
            raise serializers.ValidationError({'error':'Email Already Exist'})
        if CustomUser.objects.filter(username__iexact=attrs['username']):
               raise serializers.ValidationError({'error':'Username Already Exist'})
        return attrs
    

    def create(self, validated_data):
        user=CustomUser.objects.create(
            **validated_data
        )
        user.set_password(validated_data['password'])
        user.save()
        user.confirm_password=user.password
        return user
    


"""
A custom Login Serializer where users login with Email And Password only

"""
class LoginSerializer(AuthTokenSerializer):
    username = None
    email = serializers.CharField(
        label=_("Email"),
        write_only=True
    )
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                username=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                # msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError({'error':'login provided credentials does not exist'}, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

    

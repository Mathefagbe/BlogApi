from .models import Comment
from rest_framework import serializers
from account.serializers import CustomUserSerializer
from django.utils import timesince


class CommentPostSerializer(serializers.ModelSerializer):
    author=CustomUserSerializer(read_only=True)
    time_ago=serializers.SerializerMethodField()
    class Meta:
        model=Comment
        exclude=['id','post']


    def get_time_ago(self,obj):
       timeAgo=timesince.timesince(obj.comment_date)
       formatedTime=timeAgo.split(',')[0]
       return  f"{formatedTime} ago"

    def create(self, validated_data):
        comment=self.Meta.model.objects\
            .create(post=self.context['post'],author=self.context['user'],**validated_data)
        return comment
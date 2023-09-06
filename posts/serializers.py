from .models import BlogPost
from rest_framework import serializers
from account.serializers import CustomUserSerializer
from django.utils import timesince


class BlogDetailSerializer(serializers.ModelSerializer):
    author=CustomUserSerializer(read_only=True)
    comment_count=serializers.SerializerMethodField()
    like=serializers.SerializerMethodField()
    time_ago=serializers.SerializerMethodField()
    class Meta:
        model=BlogPost
        fields=['author','title','body','image','slug',
                'comment_count','like','time_ago']

    def get_comment_count(self,obj):
        return obj.comment.count()
    
    def get_like(self,obj):
        return obj.liked_post.filter(post_id=obj).count()

    def get_time_ago(self,obj):
       timeAgo=timesince.timesince(obj.published_date)
       formatedTime=timeAgo.split(',')[0]
       return  f"{formatedTime} ago"
     
        
class PostListSerializer(serializers.ModelSerializer):
    author=CustomUserSerializer(read_only=True)
    time_ago=serializers.SerializerMethodField()
    class Meta:
        model=BlogPost
        fields=['author','title','image','body','slug','time_ago',]
        extra_kwargs={
            'slug':{
            'read_only':True,
            },
        }
       
    def get_time_ago(self,obj):
       timeAgo=timesince.timesince(obj.published_date)
       formatedTime=timeAgo.split(',')[0]
       return  f"{formatedTime} ago"
   
    def create(self, validated_data):
        create_post=self.Meta.model.objects\
            .create(author=self.context['user'],**validated_data)
        return create_post
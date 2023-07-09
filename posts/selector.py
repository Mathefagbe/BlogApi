from rest_framework.response import Response
from rest_framework import status
def get_post_status(self):
        instance = self.get_object()
        context={}
        serializer = self.get_serializer(instance)
        # using related name to check if the using is following the author of the post
        if self.request.user.login_user.filter(user_to=instance.author).exists():
                if instance.liked_post.filter(user=self.request.user).exists():
                        context=dict(zip(['post','likestatus','status'],[ serializer.data, 'liked','following']))
           
                else:
                        context=dict(zip(['post','likestatus','status'],[ serializer.data, 'unlike','following']))
        elif self.request.user==instance.author:
                if instance.liked_post.filter(user=self.request.user).exists():
                        context=dict(zip(['post','likestatus','status'],[ serializer.data, 'liked','hide']))
           
                else:
                        context=dict(zip(['post','likestatus','status'],[ serializer.data, 'unlike','hide']))
        else:
                if instance.liked_post.filter(user=self.request.user).exists():
                        context=dict(zip(['post','likestatus','status'],[ serializer.data, 'liked','follow']))
           
                else:
                        context=dict(zip(['post','likestatus','status'],[ serializer.data, 'unlike','follow']))
        return Response(context,status=status.HTTP_200_OK)

from rest_framework.response import Response
from rest_framework import status
def get_post_status(self):
        instance = self.get_object()
        context={}
        serializer = self.get_serializer(instance) 
        if instance.author in self.request.user.following.all():
                if self.request.user in instance.like.all(): 
                        context=dict(zip(['post','likestatus','status'],[ serializer.data, 'liked','following']))
           
                else:
                        context=dict(zip(['post','likestatus','status'],[ serializer.data, 'unlike','following']))
        else:
                if self.request.user in instance.like.all(): 
                        context=dict(zip(['post','likestatus','status'],[ serializer.data, 'liked','follow']))
           
                else:
                        context=dict(zip(['post','likestatus','status'],[ serializer.data, 'unlike','follow']))
        return Response(context,status=status.HTTP_200_OK)

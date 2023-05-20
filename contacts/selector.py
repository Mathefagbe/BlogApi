from rest_framework.response import Response
from rest_framework import status
def get_following_list(self):
        followings=[]
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        for following in queryset:
            serializer = self.get_serializer(following) 
            context=dict(zip(['user_to','status'],[serializer.data['user_to'],'following'])) 
            followings.append(context)
        if page is not None:
            return self.get_paginated_response(followings)
        return Response(followings)

def get_follower_list(self):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        following=[]
        for follower in queryset:
            if follower.user_from in self.request.user.following.all():
                serializer = self.get_serializer(follower) 
                context=dict(zip(['user_from','status'],[serializer.data['user_from'],'following'])) 
                following.append(context)
            else:
                serializer = self.get_serializer(follower) 
                context=dict(zip(['user_from','status'],[serializer.data['user_from'],'follow'])) 
                following.append(context)
        if page is not None:
              return self.get_paginated_response(following)
        return Response(following,status=status.HTTP_200_OK)





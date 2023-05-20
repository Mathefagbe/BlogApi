from django.shortcuts import get_object_or_404
from posts.models import BlogPost
from rest_framework.response import Response


def get_like(self):
        post_id=self.kwargs['slug']
        post=get_object_or_404(BlogPost,slug=post_id)
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        if self.request.user in post.like.all():
            context=dict(zip(['users','status'],[ len(serializer.data), 'liked']))
            return Response(context)
        else:
            context=dict(zip(['users','status'],[ len(serializer.data), 'unlike']))
            return Response(context)
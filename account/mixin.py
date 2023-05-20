from datetime import timezone
from rest_framework.permissions import AllowAny
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login
from .serializers import LoginSerializer
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth.signals import user_logged_in
from rest_framework import status


class LoginMixin(KnoxLoginView):
    permission_classes = (AllowAny,)
    
    def get_user_token(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            return self.post_user(request, format=None)
    
    def post_user(self, request, format=None):
        token_limit_per_user = super().get_token_limit_per_user()
        if token_limit_per_user is not None:
            now = timezone.now()
            token = request.user.auth_token_set.filter(expiry__gt=now)
            if token.count() >= token_limit_per_user:
                return Response(
                    {"error": "Maximum amount of tokens allowed per user exceeded."},
                    status=status.HTTP_403_FORBIDDEN
                )
        token_ttl = super().get_token_ttl()
        instance, token = AuthToken.objects.create(request.user, token_ttl)
        user_logged_in.send(sender=request.user.__class__,
                            request=request, user=request.user)
        data = super().get_post_response_data(request, token, instance)
        return Response(data,status=status.HTTP_201_CREATED)
    

from rest_framework.generics import CreateAPIView
from .serializers import UserRegistrationSerializer,LoginSerializer
from rest_framework.permissions import IsAuthenticated
from knox.views import LogoutAllView as KnoxLogoutView
from .mixin import LoginMixin
from drf_yasg.utils import swagger_auto_schema
from utilis.apiexception import error_handler
from rest_framework.response import Response
from rest_framework import status
# from django.contrib.auth.views import LoginView


class LoginView(LoginMixin):
    @swagger_auto_schema(
            operation_summary='login with user credentials using email and password',
            operation_description="This returns a token after user have been authenticated",
            request_body=LoginSerializer
    )
    def post(self, request, format=None):
        return super().get_user_token(request)
        

class UserSignupApiView(LoginMixin,
                        CreateAPIView):
    serializer_class=UserRegistrationSerializer

    @swagger_auto_schema(
            operation_summary='signup with new credentials',
            operation_description="This returns a token after user have been authenticated"
    )
    def post(self, request, *args, **kwargs):
        try:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
        except Exception as e:
                return Response(data={
                  'detail':error_handler(e)
             },status=status.HTTP_400_BAD_REQUEST)
        return super().get_user_token(request)   

  
class LogoutView(KnoxLogoutView):
    permission_classes = (IsAuthenticated,)


    

    




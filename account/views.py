from rest_framework.generics import CreateAPIView
from .serializers import UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from knox.views import LogoutView as KnoxLogoutView
from django.contrib.auth.signals import user_logged_out
from .mixin import LoginMixin
from drf_yasg.utils import swagger_auto_schema
from utilis.apiexception import error_handler
from rest_framework.response import Response
from rest_framework import status
# from django.contrib.auth.views import LoginView


class LoginView(LoginMixin):
    
    @swagger_auto_schema(
            operation_summary='login with user credentials',
            operation_description="This returns a token after user have been authenticated"
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



# class UserListApiView(ListAPIView):
#     queryset=CustomUser.objects.all()
#     serializer_class=CustomUserSerializer
#     permission_classes=[IsAuthenticated]

    

    




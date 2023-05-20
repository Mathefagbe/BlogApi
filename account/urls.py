from django.urls import path
from .views import UserSignupApiView
from .views import LoginView,LogoutView


urlpatterns = [
    path('signup/' ,UserSignupApiView.as_view(),name='signup'),
    # path('users/',UserListApiView.as_view(),name='users'),
    path('auth/login/',LoginView.as_view(),name='knox_login'),
    path('auth/logout/',LogoutView.as_view(),name='knox_logout')
]
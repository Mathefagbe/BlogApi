from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

class EmailBackend:
    
    # a custom emailbackend that authenticate user based on the email address
    def authenticate(self,request,username=None,password=None,*args,**kwargs):
        customUser=get_user_model()
        try:
            user=customUser.objects.get(email=username)
            if getattr(user, "is_active", False) and user.check_password(password):
                return user
            return None
        except (customUser.DoesNotExist,customUser.MultipleObjectsReturned):
            return None

            
    # a function that get the user after it has been authenticated
    def get_user(self, user_id):
        customUser=get_user_model()
        try:
            user = customUser.objects.get(pk=user_id)
            return user
        except customUser.DoesNotExist:
            return None


 

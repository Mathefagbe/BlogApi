from django.db import models
from django.conf import settings
from django.utils import timezone

class UserProfile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='userprofile',db_constraint=False)
    image=models.ImageField(upload_to='profile/',default="profile/user.png")
    bio=models.TextField(blank=True)
    date_register=models.DateField(default=timezone.now)


    
    def __str__(self) -> str:
        return self.user.username
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from contacts.models import Contact



# Create your models here.

class CustomUser(AbstractUser):
   username=models.CharField(max_length=150)
   confirm_password=models.CharField(max_length=30,null=True)

   class Meta:
        indexes = [
        models.Index(fields=['id',]),
            ]

 
   
  
   
from typing import Collection, Optional
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email=models.CharField(max_length=20,unique=True)
    username=models.CharField(max_length=150)
    confirm_password=models.CharField(max_length=30,null=True)

    REQUIRED_FIELDS=['username']
    USERNAME_FIELD='email'
  
   
  

    class Meta:
        indexes = [
        models.Index(fields=['id',]),
            ]

    def __str__(self) -> str:
        return self.username

    def clean(self):
        self.username= self.username.title()
        return super().clean()
 
  
   
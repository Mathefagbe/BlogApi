from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

class CustomUser(AbstractUser):
   username=models.CharField(max_length=150)
   confirm_password=models.CharField(max_length=30,null=True)
   following = models.ManyToManyField('self',
            through="contacts.Contact",
            related_name='followers',
            symmetrical=False,
            db_constraint=True)
   

   class Meta:
        indexes = [
        models.Index(fields=['id',]),
            ]
             
   
  
   
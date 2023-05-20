from django.db import models
from django.conf import settings

class Contact(models.Model):
    user_from=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    user_to=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="user_friend",on_delete=models.CASCADE,null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
        models.Index(fields=['-created','user_to']),
            ]
        ordering = ['-created']

    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'
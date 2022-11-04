from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.
class Contact(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=70)
    email = models.CharField(max_length=70, blank=True)
    location = models.CharField(max_length=70, blank=True)
    is_favorite = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now=True)

    
    


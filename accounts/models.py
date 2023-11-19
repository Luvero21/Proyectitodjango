from django.db import models
from django.contrib.auth.models import User

class Extra(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name='extra')
    pais = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    
 
    
    
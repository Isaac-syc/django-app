from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class PerfilModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    name_img = models.ImageField(blank='', default='',upload_to='img_profile')
    
    class Meta:
        db_table = 'perfil'
        
    

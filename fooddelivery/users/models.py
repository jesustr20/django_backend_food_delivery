from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    #Agregar phone y type_user

    #Acceder solo con el email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager ()

class PasswordResetCode(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def is_valid(self):
        return timezone.now() < self.expires_at
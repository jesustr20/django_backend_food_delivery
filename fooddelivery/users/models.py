from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from .enums import UserTypeEnum
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    #Agregar phone y type_user
    phone_number = models.CharField(max_length=9, blank=True)
    biography = models.CharField(max_length=100, blank=True, null=True)
    type_user = models.CharField(
        max_length=15, 
        choices=[(tag.name, tag.value) for tag in UserTypeEnum],
        default=UserTypeEnum.CLIENT.name)
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
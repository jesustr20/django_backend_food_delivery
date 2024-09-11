from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    #Agregar phone y type_user

    #Acceder solo con el email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()
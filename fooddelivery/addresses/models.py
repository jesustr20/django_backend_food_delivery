from django.db import models
from users.models import User

# Create your models here.
class Address(models.Model):
    address = models.CharField(max_length=255, blank=True)
    district = models.CharField(max_length=255, blank=True)
    province = models.CharField(max_length=255, blank=True)
    department = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.address}, {self.district}"
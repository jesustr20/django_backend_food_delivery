from django.db import models
from mixins import InspectableModel

# Create your models here.
class Driver(InspectableModel, models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    vehicle_model = models.CharField(max_length=100)
    vehicle_plate = models.CharField(max_length=10)
    vehicle_color = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.name}"
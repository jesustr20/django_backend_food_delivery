from django.db import models
from restaurants.models import Restaurant

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="menus")

    def __str__(self) -> str:
        return self.name
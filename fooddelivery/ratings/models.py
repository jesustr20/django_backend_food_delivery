from django.db import models
from users.models import User
from restaurants.models import Restaurant
# Create your models here.

class Rating(models.Model):
    score = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="ratings", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.score} by {self.user.first_name} for self.restaruant.name"
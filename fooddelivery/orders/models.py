from django.db import models
from mixins import InspectableModel
from users.models import User
from drivers.models import Driver
from restaurants.models import Restaurant
# Create your models here.

class Order(InspectableModel, models.Model):
    status = models.CharField(max_length=50)
    order_total = models.IntegerField(null=True)
    delivery_status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True, related_name="orders")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="orders")

    def __str__(self):
        return f"Order {self.id} by {self.user.first_name}"

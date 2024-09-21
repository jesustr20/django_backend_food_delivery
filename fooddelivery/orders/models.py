from django.db import models
from users.models import User
# Create your models here.

class Order(models.Model):
    status = models.CharField(max_length=50)
    order_total = models.IntegerField(null=True)
    delivery_status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id} by {self.user.first_name}"

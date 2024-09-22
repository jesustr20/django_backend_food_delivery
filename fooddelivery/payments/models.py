from django.db import models
from orders.models import Order

# Create your models here.

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Payment {self.id} for Order {self.order.id}"

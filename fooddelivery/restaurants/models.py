from django.contrib.contenttypes.fields import GenericRelation
from mixins import InspectableModel
from django.db import models
from ratings.models import Rating
from addresses.models import Address

# Create your models here.
class Restaurant(InspectableModel, models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    ratings = GenericRelation(Rating)
    addresses = GenericRelation(Address)

    def __str__(self) -> str:
        return self.name

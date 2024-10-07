from django.db import models
from mixins import InspectableModel
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from users.models import User
# Create your models here.

class Rating(InspectableModel, models.Model):
    score = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    content_type=models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self) -> str:
        return f"{self.score} by {self.user.first_name} for {self.content_object.name if self.content_object else 'Unknown'}"
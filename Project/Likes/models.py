from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class likedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numberOfLikes = models.BigIntegerField(User, default=0)
    # contentType = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    objectID = models.PositiveIntegerField()
    # contentObject = GenericForeignKey()
# Create your models here.

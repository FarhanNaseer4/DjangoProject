from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class tags(models.Model):
    label = models.CharField(max_length=255)

class taggedItem(models.Model):
    tag = models.ForeignKey(tags, on_delete=models.CASCADE)
    tag_name = models.TextField(tags, default='abc')
    # contentType = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    obect_id = models.PositiveIntegerField()
    # contentObject = GenericForeignKey()
# Create your models here.

from django.db import models

# Create your models here.


class Info(models.Model):
    names = models.CharField(max_length=256)
    contact = models.IntegerField(primary_key=True)
    interests = models.CharField(max_length=256)
from django.db import models


# Create your models here.


class slider1fill(models.Model):
    image = models.ImageField(upload_to="",null=True, blank=True)


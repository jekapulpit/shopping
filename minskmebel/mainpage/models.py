from django.db import models


# Create your models here.


class slider1fill(models.Model):
    image = models.ImageField(upload_to="",null=True, blank=True)

class slider2fill(models.Model):
    title = models.CharField(max_length=40)
    discriotion = models.TextField()
    nowprice = models.CharField(max_length=10)
    prevprice = models.CharField(max_length=10)
    image = models.ImageField(upload_to="",null=True, blank=True)

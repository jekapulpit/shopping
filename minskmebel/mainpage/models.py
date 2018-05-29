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

class slider3fill(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to="",null=True, blank=True)
    discription = models.TextField()

class shops(models.Model):
    title = models.CharField(default="Neme",max_length=40)
    image = models.ImageField(upload_to="",null=True, blank=True)
    phone1 = models.CharField(default="+375445106036",max_length=40)
    phone2 = models.CharField(default="+375445106036",max_length=40)
    link = models.CharField(max_length=200)
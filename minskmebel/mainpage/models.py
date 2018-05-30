from django.db import models


# Create your models here.
class Collection(models.Model):
    title = models.CharField("Название",default="Название товара", max_length=40)
    subtitle = models.CharField("Краткое описание",default="Краткое описание", max_length=40)
    discriotion = models.TextField("Полное описание", default="Описание товара")
    properties = models.TextField("Характеристики товара", default="(длина, ширина и т.д.)")
    price = models.CharField("Цена",default="", max_length=10)
    fullprice = models.CharField("Полная цена без скидки",default="",max_length=15)
    image = models.ImageField(upload_to="", null=False, blank=True)
    image1 = models.ImageField(default=None, upload_to="", null=True, blank=True)
    image2 = models.ImageField(default=None, upload_to="", null=True, blank=True)
    image3 = models.ImageField(default=None, upload_to="", null=True, blank=True)
    image4 = models.ImageField(default=None, upload_to="", null=True, blank=True)
    image5 = models.ImageField(default=None, upload_to="", null=True, blank=True)
    image6 = models.ImageField(default=None, upload_to="", null=True, blank=True)
    image7 = models.ImageField(default=None, upload_to="", null=True, blank=True)


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


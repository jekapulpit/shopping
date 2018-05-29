from django.db import models
from mainpage.models import shops
# Create your models here.


class ShopItem(models.Model):
    ischeap = (
        ('1','да'),
        ('2', 'нет'),
    )
    title = models.CharField(default="Название товара",max_length=40)
    subtitle = models.CharField(default="Краткое описание",max_length=40)
    discriotion = models.TextField(default="Описание товара")
    price = models.CharField(default="Цена(просто число)",max_length=10)
    isdiscount = models.CharField("нет",max_length=3, choices=ischeap)
    seller = models.ForeignKey(shops, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="",null=False, blank=True)

from django.db import models
from mainpage.models import shops
from mainpage.models import Collection

# Create your models here.




class ShopItem(models.Model):
    ischeap = (
        ('1','да'),
        ('2', 'нет'),
    )
    categoryTemplate = (
        ('1', 'Мягкая мебель'),
        ('2', 'Гостиная'),
        ('3', 'Спальня'),
        ('4', 'Кухня'),
        ('5', 'Столовая'),
        ('6', 'Прихожая'),
        ('7', 'Ванная'),
        ('8', 'Детская'),
        ('9', 'Рабочий кабинет'),
    )
    title = models.CharField(default="Название товара",max_length=40)
    subtitle = models.CharField(default="Краткое описание",max_length=40)
    discriotion = models.TextField(default="Описание товара")
    price = models.FloatField(default=0.00)
    isdiscount = models.CharField("популярный?",max_length=3, choices=ischeap)
    seller = models.ForeignKey(shops, on_delete=models.CASCADE)
    Category = models.CharField("Категория",default='Мягкая мебель',max_length=20, choices=categoryTemplate)
    inCollection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="",null=False, blank=True)
    image1 = models.ImageField(default=None,upload_to="",null=True, blank=True)
    image2 = models.ImageField(default=None,upload_to="",null=True, blank=True)
    image3 = models.ImageField(default=None,upload_to="",null=True, blank=True)
    image4 = models.ImageField(default=None,upload_to="",null=True, blank=True)
    image5 = models.ImageField(default=None,upload_to="",null=True, blank=True)
    image6 = models.ImageField(default=None,upload_to="",null=True, blank=True)
    image7 = models.ImageField(default=None,upload_to="",null=True, blank=True)
    image8 = models.ImageField(default=None,upload_to="",null=True, blank=True)
    def IsFileExist(self):
        try:
            res = self.image.size
        except:
            res = False
        return res
    def __str__(self):
        return self.title

class discounts(models.Model):
    tovar = models.ForeignKey(ShopItem, on_delete=models.CASCADE)
    nowprice = models.FloatField("Цена со скидкой")


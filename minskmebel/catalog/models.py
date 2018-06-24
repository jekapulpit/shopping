from django.db import models
from mainpage.models import shops
from mainpage.models import Collection

# Create your models here.




class ShopItem(models.Model):
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
    title = models.CharField("Название товара",max_length=40)
    subtitle = models.CharField("Краткое описание",max_length=40)
    discriotion = models.TextField("Описание товара")
    size = models.CharField("Размеры",max_length=40, default=None, blank=True)
    matherial = models.CharField("Материал",max_length=40, default=None, blank=True)
    color = models.CharField("Цвета",max_length=40, default=None, blank=True)
    qualities = models.TextField("Доп. характеристики", default=None, blank=True)


    price = models.FloatField("Цена",default=0.00)
    isdiscount = models.BooleanField("На скидке?", default=False)
    newprice = models.FloatField("Новая цена (Если товар не на скидке, пожалуйста, укажите цену, равную обычной)", default=0.00);
    seller = models.ForeignKey(shops, on_delete=models.CASCADE, verbose_name="Поставщик")
    Category = models.CharField("Категория",default='Мягкая мебель',max_length=20, choices=categoryTemplate)
    inCollection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True, verbose_name="Коллекция", blank=True)
    image = models.ImageField("Главное фото (обязательно)",upload_to="",null=False, blank=False)
    image1 = models.ImageField("Доп. фото (Необязательно)",default=None,upload_to="",null=True, blank=True)
    image2 = models.ImageField("Доп. фото (Необязательно)",default=None,upload_to="",null=True, blank=True)
    image3 = models.ImageField("Доп. фото (Необязательно)",default=None,upload_to="",null=True, blank=True)
    image4 = models.ImageField("Доп. фото (Необязательно)",default=None,upload_to="",null=True, blank=True)
    image5 = models.ImageField("Доп. фото (Необязательно)",default=None,upload_to="",null=True, blank=True)
    image6 = models.ImageField("Доп. фото (Необязательно)",default=None,upload_to="",null=True, blank=True)
    image7 = models.ImageField("Доп. фото (Необязательно)",default=None,upload_to="",null=True, blank=True)
    image8 = models.ImageField("Доп. фото (Необязательно)",default=None,upload_to="",null=True, blank=True)

    def IsFileExist(self):
        try:
            res = self.image.size
        except:
            res = False
        return res
    def __str__(self):
        return self.title




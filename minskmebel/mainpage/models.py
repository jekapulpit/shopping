from django.db import models
from datetime import datetime, date, time
# Create your models here.
class shops(models.Model):
    title = models.CharField("Название",default="Neme",max_length=40)
    discription = models.TextField("Описание",default="Описание магазина")
    image = models.ImageField("Мини-логотип", upload_to="",null=True, blank=True)
    mainimage = models.ImageField("Полная картинка",upload_to="",null=True, blank=True, default=None)
    phone1 = models.CharField("Телефон1",default="+375445106036",max_length=40, blank=False)
    phone2 = models.CharField("Телефон2 (необязательно)",default="",max_length=40, blank=True)
    worktime = models.CharField("Время работы", default="Пн.-Пт.: ...", max_length=50)
    link = models.CharField("Ссылка на магазин", default="vegas.by", max_length=50)

    def __str__(self):
        return self.title

class Collection(models.Model):
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
    title = models.CharField("Название",default="Название товара", max_length=40)
    subtitle = models.CharField("Краткое описание",default="Краткое описание", max_length=40)
    discriotion = models.TextField("Полное описание", default="Описание товара")
    size = models.CharField("Размеры",max_length=40, default=None)
    matherial = models.CharField("Материал",max_length=40, default=None)
    color = models.CharField("Цвета",max_length=40, default=None)
    qualities = models.TextField("Доп. характеристики", default=None)

    price = models.FloatField("Цена",default='', max_length=10)
    Category = models.CharField("Категория",default='Мягкая мебель',max_length=20, choices=categoryTemplate)
    fullprice = models.CharField("Полная цена без скидки",default="",max_length=15)
    seller = models.ForeignKey(shops, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to="", null=False, blank=False)
    image1 = models.ImageField(default=None, upload_to="", null=True, blank=True)
    image2 = models.ImageField(default=None, upload_to="", null=True, blank=True)
    image3 = models.ImageField(default=None, upload_to="", null=True, blank=True)
    image4 = models.ImageField(default=None, upload_to="", null=True, blank=True)
    image5 = models.ImageField(default=None, upload_to="", null=True, blank=True)
    image6 = models.ImageField(default=None, upload_to="", null=True, blank=True)
    image7 = models.ImageField(default=None, upload_to="", null=True, blank=True)
    def __str__(self):
        return self.title


class slider1fill(models.Model):
    image = models.ImageField(upload_to="",null=True, blank=True)
    link = models.CharField("Ссылка на товар либо новость", max_length=100, default='/catalog')



class Sale(models.Model):
    title = models.CharField("Заголовок акции", max_length=40)
    discriotion = models.TextField("Описание")
    image = models.ImageField("Картинка",upload_to="", null=True, blank=True)

    def __str__(self):
        return self.title

class New(models.Model):
    title = models.CharField("Заголовок новости", max_length=40)
    image = models.ImageField("Картинка", upload_to="", null=True, blank=True)
    date = models.DateField("Дата", default=datetime.today())
    discriotion = models.TextField("Текст новости")
    def __str__(self):
        return self.title
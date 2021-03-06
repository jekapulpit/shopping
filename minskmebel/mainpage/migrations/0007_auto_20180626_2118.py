# Generated by Django 2.0.5 on 2018-06-26 18:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0006_auto_20180625_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='color',
            field=models.CharField(blank=True, default=None, max_length=40, verbose_name='Цвета'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='matherial',
            field=models.CharField(blank=True, default=None, max_length=40, verbose_name='Материал'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='qualities',
            field=models.TextField(blank=True, default=None, verbose_name='Доп. характеристики'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='size',
            field=models.CharField(blank=True, default=None, max_length=40, verbose_name='Размеры'),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 6, 26, 21, 18, 9, 730478), verbose_name='Дата'),
        ),
    ]

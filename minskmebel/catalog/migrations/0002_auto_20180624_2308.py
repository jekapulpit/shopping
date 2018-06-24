# Generated by Django 2.0.5 on 2018-06-24 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopitem',
            name='color',
            field=models.CharField(default=None, max_length=40, verbose_name='Цвета'),
        ),
        migrations.AlterField(
            model_name='shopitem',
            name='matherial',
            field=models.CharField(default=None, max_length=40, verbose_name='Материал'),
        ),
        migrations.AlterField(
            model_name='shopitem',
            name='qualities',
            field=models.TextField(default=None, verbose_name='Доп. характеристики'),
        ),
        migrations.AlterField(
            model_name='shopitem',
            name='size',
            field=models.CharField(default=None, max_length=40, verbose_name='Размеры'),
        ),
    ]

# Generated by Django 2.0.5 on 2018-06-01 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0007_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='shops',
            name='mainimage',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name='Полная картинка'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='discription',
            field=models.TextField(default='Описание магазина', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Мини-логотип'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='phone1',
            field=models.CharField(default='+375445106036', max_length=40, verbose_name='Телефон Velcom'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='phone2',
            field=models.CharField(default='+375445106036', max_length=40, verbose_name='Телефон МТС'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='title',
            field=models.CharField(default='Neme', max_length=40, verbose_name='Название'),
        ),
    ]
# Generated by Django 2.0.5 on 2018-06-25 14:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_auto_20180624_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='shops',
            name='phone2',
            field=models.CharField(blank=True, default='+375445106036', max_length=40, verbose_name='Телефон2 (необязательно)'),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 6, 25, 17, 37, 18, 260493), verbose_name='Дата'),
        ),
    ]
# Generated by Django 2.0.5 on 2018-06-01 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20180601_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopitem',
            name='isdiscount',
            field=models.BooleanField(default=False, verbose_name='На свидке?'),
        ),
        migrations.AlterField(
            model_name='shopitem',
            name='newprice',
            field=models.FloatField(default=models.FloatField(default=0.0), verbose_name='Новая цена'),
        ),
    ]

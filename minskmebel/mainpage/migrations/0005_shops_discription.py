# Generated by Django 2.0.5 on 2018-05-30 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_remove_shops_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='shops',
            name='discription',
            field=models.TextField(default='Описание магазина'),
        ),
    ]

# Generated by Django 2.0.5 on 2018-05-30 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20180530_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopitem',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]

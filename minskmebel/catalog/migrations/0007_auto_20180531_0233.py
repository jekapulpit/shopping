# Generated by Django 2.0.5 on 2018-05-30 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_discounts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopitem',
            name='isdiscount',
            field=models.CharField(choices=[('1', 'да'), ('2', 'нет')], max_length=3, verbose_name='популярный?'),
        ),
    ]

# Generated by Django 2.0.5 on 2018-05-29 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainpage', '0005_auto_20180529_2350'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Название товара', max_length=40)),
                ('subtitle', models.CharField(default='Краткое описание', max_length=40)),
                ('discriotion', models.TextField(default='Описание товара')),
                ('price', models.CharField(default='Цена(просто число)', max_length=10)),
                ('isdiscount', models.CharField(choices=[('1', 'да'), ('2', 'нет')], max_length=3, verbose_name='нет')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.shops')),
            ],
        ),
    ]
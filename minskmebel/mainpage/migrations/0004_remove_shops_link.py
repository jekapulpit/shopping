# Generated by Django 2.0.5 on 2018-05-30 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_collection_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shops',
            name='link',
        ),
    ]

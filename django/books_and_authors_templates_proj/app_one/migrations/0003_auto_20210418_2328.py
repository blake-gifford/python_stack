# Generated by Django 2.2.4 on 2021-04-18 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_auto_20210418_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(default='blank', max_length=255),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(default='blank', max_length=255),
        ),
    ]

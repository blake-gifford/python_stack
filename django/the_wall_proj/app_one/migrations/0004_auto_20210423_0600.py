# Generated by Django 2.2.4 on 2021-04-23 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0003_remove_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

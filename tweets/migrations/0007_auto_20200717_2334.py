# Generated by Django 3.0.8 on 2020-07-17 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0006_auto_20200717_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='likes',
            field=models.BooleanField(default=False),
        ),
    ]

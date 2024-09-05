# Generated by Django 5.0.6 on 2024-09-01 11:36

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Likes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='likeditem',
            name='numberOfLikes',
            field=models.BigIntegerField(default=0, verbose_name=django.contrib.auth.models.User),
        ),
    ]

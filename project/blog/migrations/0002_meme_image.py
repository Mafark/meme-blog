# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meme',
            name='image',
            field=models.ImageField(default=None, upload_to='uploads/'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-01 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20180401_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, default='profile/no-img.jpg', null=True, upload_to='profile/picture/'),
        ),
    ]

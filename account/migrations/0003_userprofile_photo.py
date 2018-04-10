# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-01 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userprofile_join_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, default='/media/no-img.jpg', null=True, upload_to='profile/picture/'),
        ),
    ]
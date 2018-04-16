# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-16 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20180416_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='member_type',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='farmer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='investor',
            field=models.BooleanField(default=False),
        ),
    ]

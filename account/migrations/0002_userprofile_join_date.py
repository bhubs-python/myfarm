# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-29 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='join_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

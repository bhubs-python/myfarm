# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-17 06:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_credit_creditrecharge_credittransfer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='country',
        ),
    ]

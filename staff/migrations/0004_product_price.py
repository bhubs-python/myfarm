# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-10 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_product_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

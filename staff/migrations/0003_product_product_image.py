# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-09 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, default='/media/no-img.jpg', null=True, upload_to='product/'),
        ),
    ]
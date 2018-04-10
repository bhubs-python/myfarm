# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-09 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_period', models.FloatField(blank=True, null=True)),
                ('expected_return', models.FloatField(blank=True, null=True)),
                ('harvest_period', models.FloatField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=10000, null=True)),
                ('extra', models.TextField(blank=True, max_length=5000, null=True)),
                ('farm_size', models.FloatField(blank=True, null=True)),
                ('farm_location', models.TextField(blank=True, max_length=1000, null=True)),
                ('product_type', models.CharField(blank=True, max_length=255, null=True)),
                ('farm_email', models.EmailField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]

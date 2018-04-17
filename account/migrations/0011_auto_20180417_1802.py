# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-17 12:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_remove_userprofile_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditrecharge',
            name='authorized_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authorized_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='creditrecharge',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wallet_user', to=settings.AUTH_USER_MODEL),
        ),
    ]

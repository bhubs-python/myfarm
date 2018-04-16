# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-16 06:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20180410_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='member_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.MemberType'),
        ),
    ]
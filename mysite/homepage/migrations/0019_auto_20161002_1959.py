# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-02 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0018_auto_20161002_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activa',
            name='otp',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='activa',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]

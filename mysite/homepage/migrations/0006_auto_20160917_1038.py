# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-17 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_myusr_house'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myusr',
            name='house',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
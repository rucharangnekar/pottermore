# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-17 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20160916_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='myusr',
            name='house',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]

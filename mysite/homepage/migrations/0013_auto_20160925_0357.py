# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-25 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_myusr_level4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myusr',
            name='ranktemp',
        ),
        migrations.AddField(
            model_name='myusr',
            name='totals2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='myusr',
            name='totals3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='myusr',
            name='totals4',
            field=models.IntegerField(default=0),
        ),
    ]
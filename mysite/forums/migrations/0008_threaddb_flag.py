# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-26 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0007_auto_20160926_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='threaddb',
            name='flag',
            field=models.IntegerField(default=0),
        ),
    ]

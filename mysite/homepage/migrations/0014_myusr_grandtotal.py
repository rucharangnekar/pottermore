# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-25 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0013_auto_20160925_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='myusr',
            name='grandtotal',
            field=models.IntegerField(default=0),
        ),
    ]
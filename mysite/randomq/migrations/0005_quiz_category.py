# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-18 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomq', '0004_rquiz_tanswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='category',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]

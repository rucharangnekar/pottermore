# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-26 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0005_threaddb_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='threaddb',
            name='postid',
            field=models.IntegerField(default=0),
        ),
    ]

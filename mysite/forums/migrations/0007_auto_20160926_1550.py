# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-26 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0006_threaddb_postid'),
    ]

    operations = [
        migrations.AddField(
            model_name='threaddb',
            name='dislike',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='threaddb',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]

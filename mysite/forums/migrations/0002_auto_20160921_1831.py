# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumdb',
            name='posts',
        ),
        migrations.AddField(
            model_name='threaddb',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-25 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0002_auto_20160921_1831'),
    ]

    operations = [
        migrations.RenameField(
            model_name='threaddb',
            old_name='count',
            new_name='counting',
        ),
        migrations.AddField(
            model_name='forumdb',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]

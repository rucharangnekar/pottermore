# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-27 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0009_forumdb_fid'),
    ]

    operations = [
        migrations.AddField(
            model_name='threaddb',
            name='foid',
            field=models.IntegerField(default=0),
        ),
    ]
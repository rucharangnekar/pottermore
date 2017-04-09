# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-02 15:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0020_activa_user1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activa',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activa',
            name='user1',
            field=models.CharField(max_length=100),
        ),
    ]

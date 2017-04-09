# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-16 11:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='usr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score1', models.IntegerField(default=0)),
                ('score2', models.IntegerField(default=0)),
                ('score3', models.IntegerField(default=0)),
                ('score4', models.IntegerField(default=0)),
                ('tempscore', models.IntegerField(default=0)),
                ('keym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

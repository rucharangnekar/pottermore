# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-02 13:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0017_myusr_bonfl'),
    ]

    operations = [
        migrations.CreateModel(
            name='activa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.FileField(blank=True, max_length=500, upload_to=''),
        ),
    ]

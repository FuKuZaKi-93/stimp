# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_auto_20171128_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
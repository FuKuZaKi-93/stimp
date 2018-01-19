# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-19 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0006_auto_20180109_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='rate_ave',
            field=models.IntegerField(default=0, verbose_name='評価平均'),
        ),
        migrations.AddField(
            model_name='img',
            name='rate_sum',
            field=models.IntegerField(default=0, verbose_name='評価累計'),
        ),
        migrations.AddField(
            model_name='img',
            name='rated',
            field=models.IntegerField(default=0, verbose_name='評価者数'),
        ),
    ]
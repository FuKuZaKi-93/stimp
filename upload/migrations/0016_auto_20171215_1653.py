# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 07:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0015_auto_20171205_2013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='target',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='img',
            name='category',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
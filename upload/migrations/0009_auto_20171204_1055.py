# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0008_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True, verbose_name=''),
        ),
    ]

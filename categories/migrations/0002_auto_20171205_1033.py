# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 01:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='theme',
            old_name='theme',
            new_name='title',
        ),
    ]

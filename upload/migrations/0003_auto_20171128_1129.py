# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 02:29
from __future__ import unicode_literals

from django.db import migrations, models
import upload.models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20171128_0958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='img',
            name='terminated_at',
        ),
        migrations.RemoveField(
            model_name='img',
            name='user',
        ),
        migrations.AlterField(
            model_name='img',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='作成日'),
        ),
        migrations.AlterField(
            model_name='img',
            name='file',
            field=models.ImageField(upload_to=upload.models.get_image_path, verbose_name='ファイル'),
        ),
        migrations.AlterField(
            model_name='img',
            name='title',
            field=models.CharField(blank=True, max_length=255, verbose_name='タイトル'),
        ),
        migrations.AlterField(
            model_name='img',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日'),
        ),
    ]
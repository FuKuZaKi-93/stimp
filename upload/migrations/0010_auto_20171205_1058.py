# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0009_auto_20171204_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='item1_1',
            field=models.CharField(blank=True, choices=[('item1-1', 'item1-1'), ('item1_2', 'item1_2'), ('item1-3', 'item1-3'), ('item1_4', 'item1_4'), ('item1-5', 'item1-5'), ('item1_6', 'item1_6'), ('item1-7', 'item1-7'), ('item1_8', 'item1_8'), ('item1-9', 'item1-9'), ('item1_10', 'item1_10')], max_length=255, verbose_name='上半身1'),
        ),
        migrations.AddField(
            model_name='img',
            name='item1_2',
            field=models.CharField(blank=True, choices=[('item1-1', 'item1-1'), ('item1_2', 'item1_2'), ('item1-3', 'item1-3'), ('item1_4', 'item1_4'), ('item1-5', 'item1-5'), ('item1_6', 'item1_6'), ('item1-7', 'item1-7'), ('item1_8', 'item1_8'), ('item1-9', 'item1-9'), ('item1_10', 'item1_10')], max_length=255, verbose_name='上半身2'),
        ),
        migrations.AddField(
            model_name='img',
            name='item1_3',
            field=models.CharField(blank=True, choices=[('item1-1', 'item1-1'), ('item1_2', 'item1_2'), ('item1-3', 'item1-3'), ('item1_4', 'item1_4'), ('item1-5', 'item1-5'), ('item1_6', 'item1_6'), ('item1-7', 'item1-7'), ('item1_8', 'item1_8'), ('item1-9', 'item1-9'), ('item1_10', 'item1_10')], max_length=255, verbose_name='上半身3'),
        ),
        migrations.AddField(
            model_name='img',
            name='item1_4',
            field=models.CharField(blank=True, choices=[('item1-1', 'item1-1'), ('item1_2', 'item1_2'), ('item1-3', 'item1-3'), ('item1_4', 'item1_4'), ('item1-5', 'item1-5'), ('item1_6', 'item1_6'), ('item1-7', 'item1-7'), ('item1_8', 'item1_8'), ('item1-9', 'item1-9'), ('item1_10', 'item1_10')], max_length=255, verbose_name='上半身4'),
        ),
        migrations.AddField(
            model_name='img',
            name='item2_1',
            field=models.CharField(blank=True, choices=[('item2-1', 'item2-1'), ('item2_2', 'item2_2'), ('item2-3', 'item2-3'), ('item2_4', 'item2_4'), ('item2-5', 'item2-5'), ('item2_6', 'item2_6'), ('item2-7', 'item2-7'), ('item2_8', 'item2_8'), ('item2-9', 'item2-9'), ('item2_10', 'item2_10')], max_length=255, verbose_name='下半身1'),
        ),
        migrations.AddField(
            model_name='img',
            name='item2_2',
            field=models.CharField(blank=True, choices=[('item2-1', 'item2-1'), ('item2_2', 'item2_2'), ('item2-3', 'item2-3'), ('item2_4', 'item2_4'), ('item2-5', 'item2-5'), ('item2_6', 'item2_6'), ('item2-7', 'item2-7'), ('item2_8', 'item2_8'), ('item2-9', 'item2-9'), ('item2_10', 'item2_10')], max_length=255, verbose_name='下半身2'),
        ),
        migrations.AddField(
            model_name='img',
            name='item2_3',
            field=models.CharField(blank=True, choices=[('item2-1', 'item2-1'), ('item2_2', 'item2_2'), ('item2-3', 'item2-3'), ('item2_4', 'item2_4'), ('item2-5', 'item2-5'), ('item2_6', 'item2_6'), ('item2-7', 'item2-7'), ('item2_8', 'item2_8'), ('item2-9', 'item2-9'), ('item2_10', 'item2_10')], max_length=255, verbose_name='下半身3'),
        ),
    ]

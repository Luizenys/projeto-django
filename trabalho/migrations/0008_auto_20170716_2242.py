# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-17 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabalho', '0007_auto_20170716_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shows',
            name='local',
            field=models.CharField(max_length=200, verbose_name='Local'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-16 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabalho', '0003_auto_20170716_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shows',
            name='texto',
        ),
        migrations.AddField(
            model_name='shows',
            name='data',
            field=models.CharField(default='05/07/2017', max_length=10, verbose_name='Data'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-16 22:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trabalho', '0002_auto_20170716_1928'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Excursao',
            new_name='Shows',
        ),
        migrations.AlterModelOptions(
            name='shows',
            options={'verbose_name': 'Show', 'verbose_name_plural': 'Shows'},
        ),
    ]

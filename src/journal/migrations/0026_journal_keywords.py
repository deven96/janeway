# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-29 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0032_auto_20190304_0916'),
        ('journal', '0025_auto_20190326_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='keywords',
            field=models.ManyToManyField(blank=True, null=True, to='submission.Keyword'),
        ),
    ]

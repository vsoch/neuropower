# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neuropowertoolbox', '0016_auto_20160217_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametermodel',
            name='SID',
            field=models.CharField(default='', max_length=300),
        ),
    ]

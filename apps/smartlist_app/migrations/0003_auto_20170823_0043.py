# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-23 00:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartlist_app', '0002_auto_20170822_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='snippet',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AlterField(
            model_name='resource',
            name='link',
            field=models.CharField(max_length=255),
        ),
    ]

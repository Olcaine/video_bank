# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-09 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_bank', '0004_auto_20181108_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rented',
            field=models.BooleanField(default=False),
        ),
    ]
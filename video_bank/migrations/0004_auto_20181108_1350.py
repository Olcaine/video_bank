# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-08 12:50
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_bank', '0003_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, max_length=100, populate_from='title', unique_with=['title']),
        ),
    ]
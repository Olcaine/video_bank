# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-05 10:16
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields
import userena.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mugshot', easy_thumbnails.fields.ThumbnailerImageField(blank=True, help_text='A personal image displayed in your profile.', upload_to=userena.models.upload_to_mugshot, verbose_name='mugshot')),
                ('privacy', models.CharField(choices=[(b'open', 'Open'), (b'registered', 'Registered'), (b'closed', 'Closed')], default=b'registered', help_text='Designates who can view your profile.', max_length=15, verbose_name='privacy')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='my_profile', to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete'),
                'abstract': False,
                'permissions': (('view_profile', 'Can view profile'),),
            },
        ),
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=100, populate_from='label', unique_with=['label'])),
            ],
        ),
        migrations.CreateModel(
            name='MovieRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='video_bank.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('actors', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=25)),
                ('director', models.CharField(max_length=25)),
                ('length', models.TimeField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('release_date', models.DateField()),
                ('rented', models.BooleanField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=100, populate_from='title', unique_with=['title'])),
                ('synopsis', models.TextField()),
                ('trailer_url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='movierent',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='video_bank.Movies'),
        ),
    ]

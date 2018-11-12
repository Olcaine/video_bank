# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

choices = []

VIDEO_STATE_CHOICES = (
    ('Loué', 'Loué'),
    ('Rendu', 'Rendu'),
)

class Movie(models.Model):
    title = models.CharField(max_length=80)
    actors = models.CharField(max_length=25)
    country = models.CharField(max_length=25)
    director = models.CharField(max_length=25)
    length = models.TimeField(auto_now=False, auto_now_add=False)
    picture = models.ImageField(upload_to="articles", null=True, blank=True)
    release_date = models.DateField()
    rented = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='title', unique_with=['title'], always_update=True, max_length=100)
    synopsis = models.TextField()
    trailer_url = models.URLField()
    genre = models.ManyToManyField("MovieGenre", blank=True)

    def __unicode__ (self):
        return self.slug

class Customer(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')

class MovieRent(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True)
    movie = models.ForeignKey(Movie, null=True, blank=True)
    checkout_date = models.DateTimeField()
    return_date = models.DateTimeField()

class MovieGenre(models.Model):
    label = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='label', unique_with=['label'], max_length=100)

    def __unicode__ (self):
        return self.label

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Movie, Customer, MovieRent, MovieGenre

admin.site.register(Movie)
admin.site.register(MovieRent)
admin.site.register(MovieGenre)

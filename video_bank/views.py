# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Movie, Customer, MovieRent, MovieGenre

class MoviesListView(ListView):
    model = Movie

class MoviesDetailView(DetailView):
    model = Movie

class MoviesCreateView(CreateView):
    model = Movie
    fields = "__all__"

    def get_success_url(self):
       return reverse("movies_detail", args=[self.object.slug])

class MoviesUpdateView(UpdateView):
    model = Movie
    fields = "__all__"

    def get_success_url(self):
        return reverse("movies_detail", args=[self.object.slug])

class MoviesDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy("movies_list")

class MoviesRentListView(ListView):
    model = Movie
    template_name = "video_bank/movie_rent.html"

@method_decorator(csrf_exempt, name='dispatch')
class MoviesRentView(UpdateView):
    model = Movie
    fields = ["rented",]

    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse({
            "id": self.object.id,
            "rented": self.object.rented,
        })

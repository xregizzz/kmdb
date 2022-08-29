from django.urls import path
from . import views

urlpatterns = [
    path("movies/", views.MoviesView.as_view()),
    path("movies/<movie_id>/", views.MoviesDetailView.as_view()),
]

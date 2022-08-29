from django.urls import path
from . import views

urlpatterns = [
    path("movies/<movie_id>/reviews/", views.ReviewsView.as_view()),
    path("movies/<movie_id>/reviews/<review_id>", views.ReviewsDetailView.as_view()),
    path("movies/<movie_id>/reviews/<review_id>", views.ReviewsViewProtected.as_view()),
]

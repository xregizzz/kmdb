from django.urls import path
from . import views

urlpatterns = [
    path("users/register/", views.UserView.as_view()),
    path("users/login/", views.UserLogin.as_view()),
    path("users/", views.ProtectedUserView.as_view()),
    path("users/<user_id>", views.ProtectedUserDetailView.as_view()),
]

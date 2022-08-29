from turtle import update
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    bio = models.TextField(blank=True, null=True)
    is_critic = models.BooleanField(blank=True, null=True, default=False)
    updated_at = AutoDateTimeField(default=datetime.date.today)

    REQUIRED_FIELDS = ["birthdate", "email", "first_name", "last_name"]

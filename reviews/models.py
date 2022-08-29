from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Recomendation(models.TextChoices):
    MUST = "Must Watch"
    SHOULD = "Should Watch"
    AVOID = "Avoid Watch"
    DEFAULT = "No Opinion"


class Review(models.Model):
    stars = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    review = models.TextField()
    spoilers = models.BooleanField(blank=True, null=True, default=False)
    recomendation = models.CharField(
        max_length=50, choices=Recomendation.choices, default=Recomendation.DEFAULT
    )

    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reviews"
    )

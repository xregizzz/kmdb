from rest_framework import serializers
from .models import Review
from users.serializers import UserSerializerReview


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializerReview(read_only=True)

    class Meta:
        model = Review
        fields = [
            "id",
            "stars",
            "review",
            "spoilers",
            "movie",
            "user",
            "recomendation",
        ]

        read_only_fields = ["movie"]

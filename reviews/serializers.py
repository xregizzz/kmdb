from asyncore import write
from rest_framework import serializers
from .models import Review
from users.serializers import UserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

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
        extras_kwargs = {
            "email": {"write_only": True},
            "username": {"write_only": True},
            "birthdate": {"write_only": True},
            "bio": {"write_only": True},
            "is_critic": {"write_only": True},
            "updated_at": {"write_only": True},
            "is_superuser": {"write_only": True},
        }

        read_only_fields = ["movie"]

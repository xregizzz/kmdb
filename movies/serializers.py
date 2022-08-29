from rest_framework import serializers
from genres.serializers import GenreSerializer
from .models import Movie
from genres.models import Genre


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10)
    premiere = serializers.DateField(format="%Y-%m-%d")
    classification = serializers.IntegerField()
    synopsis = serializers.CharField(max_length=256)

    genres = GenreSerializer(many=True)

    def create(self, validated_data: dict) -> Movie:
        genres_data = validated_data.pop("genres")

        movie = Movie.objects.create(**validated_data)

        for genre in genres_data:
            genre_obj, _ = Genre.objects.get_or_create(**genre)
            movie.genres.add(genre_obj)

        return movie

    def update(self, instance: Movie, validated_data: dict) -> Movie:

        genres_data = validated_data.pop("genres")

        instance.genres.clear()

        for genre in genres_data:
            genre_obj, _ = Genre.objects.get_or_create(**genre)
            instance.genres.add(genre_obj)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

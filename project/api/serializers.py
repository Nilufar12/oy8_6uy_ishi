from rest_framework import serializers
from .models import Genre, Director, Actor, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class MovieUserSerializer(serializers.ModelSerializer):
    genre_write = serializers.ChoiceField(choices=Genre.objects.all(), read_only=True)
    director_write = serializers.ChoiceField(choices=Director.objects.all(), read_only=True)
    actor_write = serializers.ChoiceField(choices=Actor.objects.all(), read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'description', 'genres', 'directors', 'actors', 'genre_write', 'director_write', 'actor_write']
        depth = 1

    def create(self, validated_data):
        genre_write = validated_data.pop('genre_write')
        movie = Movie.objects.create(genre=genre_write, **validated_data)
        movie.save()
        return movie

    def update(self, instance, validated_data):
        instance.genre = validated_data.pop('genre') or instance.genre
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class MovieAdminSerializer(serializers.ModelSerializer):
    genre_write = serializers.ChoiceField(choices=Genre.objects.all(), read_only=True)
    director_write = serializers.ChoiceField(choices=Director.objects.all(), read_only=True)
    actor_write = serializers.ChoiceField(choices=Actor.objects.all(), read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'description', 'photo', 'genres', 'directors', 'actors', 'genre_write', 'director_write', 'actor_write']
        depth = 1

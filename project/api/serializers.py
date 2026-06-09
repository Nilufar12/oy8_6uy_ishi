from wsgiref import validate

from django.core.validators import validate_domain_name
from rest_framework import serializers
from .models import Genre, Director, Actor, Movie, Comment


class MovieSerializerForGenre(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    # movies = serializers.StringRelatedField(many=True)
    # movies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # movies = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie-detail')
    # movies = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    url = serializers.HyperlinkedIdentityField(view_name='genre-detail')

    movies = MovieSerializerForGenre(many=True)

    class Meta:
        model = Genre
        fields = '__all__'

    def create(self, validated_data):
        movies = validated_data.pop('movies')
        genres = Genre.objects.create(**validated_data)
        for movie in movies:
            Movie.objects.create(genres=genres, **movie)
        return genres

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class MovieSerializerForDirector(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    # movies = serializers.StringRelatedField(many=True)
    # movies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # movies = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie-detail')
    # movies = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    # url = serializers.HyperlinkedIdentityField(view_name='director-detail')
    movies = MovieSerializerForDirector(many=True)

    class Meta:
        model = Director
        fields = '__all__'

    def create(self, validated_data):
        movies = validated_data.pop('movies')
        director = Director.objects.create(**validated_data)
        for movie in movies:
            Director.objects.create(director=director, **movie)
        return director

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class MovieSerializerForActor(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    # movies = serializers.StringRelatedField(many=True)
    # movies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # movies = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie-detail')
    # movies = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    # url = serializers.HyperlinkedIdentityField(view_name='actor-detail')
    movies = MovieSerializerForActor(many=True)

    class Meta:
        model = Actor
        fields = '__all__'

    def create(self, validated_data):
        movies = validated_data.pop('movies')
        actor = Actor.objects.create(**validated_data)
        for movie in movies:
            Actor.objects.create(actors=actor, **movie)
        return actor

    def update(self, instance, validated_data):
        instance.f_name = validated_data.get('f_name', instance.f_name)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class MovieUserSerializer(serializers.ModelSerializer):
    genre_write = serializers.ChoiceField(choices=Genre.objects.all(), read_only=True)
    director_write = serializers.ChoiceField(choices=Director.objects.all(), read_only=True)
    actor_write = serializers.ChoiceField(choices=Actor.objects.all(), read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'description', 'genres', 'directors', 'actors', 'genre_write', 'director_write', 'actor_write']


class MovieAdminSerializer(serializers.ModelSerializer):
    genre_write = serializers.ChoiceField(choices=Genre.objects.all(), read_only=True)
    director_write = serializers.ChoiceField(choices=Director.objects.all(), read_only=True)
    actor_write = serializers.ChoiceField(choices=Actor.objects.all(), read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'description', 'photo', 'genres', 'directors', 'actors', 'genre_write']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text']
        read_only_fields = ('text',)

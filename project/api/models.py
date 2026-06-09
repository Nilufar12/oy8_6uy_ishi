from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Director(models.Model):
    full_name = models.CharField(max_length=200)
    birth_year = models.PositiveIntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Actor(models.Model):
    f_name = models.CharField(max_length=200)
    birth_year = models.PositiveIntegerField()

    def __str__(self):
        return self.f_name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='images', null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True, related_name='movies')
    actors = models.ManyToManyField(Actor, blank=True, related_name='movies')
    directors = models.ManyToManyField(Director, blank=True, related_name='movies')

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')

    def __str__(self):
        return self.text

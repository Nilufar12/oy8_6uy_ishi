from django.db import models


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
    director = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='images', null=True, blank=True)
    genres = models.ForeignKey(Genre, on_delete=models.CASCADE)
    actors = models.ForeignKey(Actor, on_delete=models.CASCADE)
    directors = models.ManyToManyField(Director, blank=True)

    def __str__(self):
        return self.title

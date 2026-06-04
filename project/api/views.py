from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import *
from .serializers import *


class GenreListAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


class DirectorListCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


class ActorListCreateAPIView(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


class MovieListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieAdminSerializer

    def get_queryset(self):
        genre_id = self.kwargs.get('genre_id')
        if genre_id:
            return self.queryset.filter(genre_id=genre_id)
        return self.queryset

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return MovieAdminSerializer
        return MovieUserSerializer


class MovieRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieAdminSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'




from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework import permissions
from rest_framework.permissions import DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

from .models import *
from .serializers import *
from .permissions import *


class GenreListAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [MyIsAuthenticatedOrReadOnly]


class GenreRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class DirectorListCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class DirectorRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class ActorListCreateAPIView(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class ActorRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class MovieListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieAdminSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

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
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class CommentListApiView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [MyIsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(movie_id=self.kwargs.get('pk'))

    def perform_create(self, serializer):
        movie = get_object_or_404(Movie, pk=self.kwargs.get('pk'))
        serializer.validated_data['user'] = self.request.user
        serializer.validated_data['movie'] = movie
        serializer.save()
        return serializer


class CommentRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'comment_id'
    permission_classes = [IsCommentOwnerOrReadOnly]

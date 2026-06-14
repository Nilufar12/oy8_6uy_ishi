from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from rest_framework.permissions import DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


class GenreAPIViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# class GenreRetrieveAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer
#     lookup_field = 'pk'
#     lookup_url_kwarg = 'pk'
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class DirectorAPIViewSet(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


# class DirectorRetrieveAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Director.objects.all()
#     serializer_class = DirectorSerializer
#     lookup_field = 'pk'
#     lookup_url_kwarg = 'pk'
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class ActorAPIViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


# class ActorRetrieveAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Actor.objects.all()
#     serializer_class = ActorSerializer
#     lookup_field = 'pk'
#     lookup_url_kwarg = 'pk'
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class MovieAPIViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieAdminSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


# class MovieRetrieveAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieAdminSerializer
#     lookup_field = 'pk'
#     lookup_url_kwarg = 'pk'
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(movie_id=self.kwargs.get('pk'))

    def perform_create(self, serializer):
        movie = get_object_or_404(Movie, pk=self.kwargs.get('movie_pk'))
        serializer.validated_data['user'] = self.request.user
        serializer.validated_data['movie'] = movie
        serializer.save()
        return serializer


# class CommentRetrieveAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     lookup_url_kwarg = 'comment_id'
#     permission_classes = [IsCommentOwnerOrReadOnly]

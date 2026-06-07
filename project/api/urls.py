from django.urls import path

from .views import MovieListCreateAPIView, DirectorListCreateAPIView, ActorListCreateAPIView, \
    MovieRetrieveAPIView, DirectorRetrieveAPIView, ActorRetrieveAPIView, GenreListAPIView, GenreRetrieveAPIView, \
    CommentListApiView, CommentRetrieveAPIView

urlpatterns = [
    path('movies/', MovieListCreateAPIView.as_view()),
    path('movies/<int:pk>/', MovieRetrieveAPIView.as_view()),
    path('movies/genres/<int:pk>/', MovieListCreateAPIView.as_view()),

    path('directors/', DirectorListCreateAPIView.as_view()),
    path('directors/<int:pk>/', DirectorRetrieveAPIView.as_view()),

    path('actors/', ActorListCreateAPIView.as_view()),
    path('actors/<int:pk>/', ActorRetrieveAPIView.as_view()),

    path('genres/', GenreListAPIView.as_view()),
    path('genres/<int:pk>/', GenreRetrieveAPIView.as_view()),

    path('movies/', CommentListApiView.as_view()),
    path('movies/<int:pk>/', CommentRetrieveAPIView.as_view()),
    path('movies/<int:pk>/comments/', CommentListApiView.as_view()),
path('movies/<int:pk>/comments/<int:comment_id>/', CommentRetrieveAPIView.as_view()),
]

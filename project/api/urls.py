from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('movies', MovieAPIViewSet)
router.register('directors', DirectorAPIViewSet)
router.register('actors', ActorAPIViewSet)
router.register('genres', GenreAPIViewSet)


urlpatterns = [
    path(
        'movies/<int:pk>/comments',
        CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='comment_list'),
    path(
        'movies/<int:movie_pk>/comments/<int:pk>/',
         CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='comment_detail'),
        
    path('', include(router.urls))
]

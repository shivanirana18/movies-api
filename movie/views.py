from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Movie
from .serializers import MovieSerializer, GenreSerializer
# Create your views here.

class MovieListCreate(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class MovieRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'primaryid'
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


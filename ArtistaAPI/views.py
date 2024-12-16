from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from ArtistaAPI.models import Artista, Musica, Album
from ArtistaAPI.serializers import ArtistaSerializer, MusicaSerializer, AlbumSerializer


class ArtistaListCreateView(generics.ListCreateAPIView):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

class ArtistaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer


class MusicaListCreateView(generics.ListCreateAPIView):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer

class MusicaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer


class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
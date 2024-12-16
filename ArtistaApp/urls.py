#from django.contrib import admin
#from django.urls import path
#from ArtistaApp import views

#urlpatterns = [
    # path('',views.index),
   # path('lista/',views.lista),
   # path('agregar/',views.registrarArtista),
    #path('eliminarArtista/<int:id>',views.eliminarArtista),
    #path('actualizarArtista/<int:id>',views.actualizarArtista),
   # path('lista2/',views.listaMusica),
    #path('agregaMusica',views.registrarMusica),
    #path('actualizaMusica/<int:id>',views.actualizarMusica),
    #path('eliminaMusica/<int:id>',views.eliminaMusica),
   # path('lista3/',views.listaAlbum),
    #path('agregaAlbum/',views.registrarAlbum),
   # path('actualizaAlbum/<int:id>',views.actualizaAlbum),
   # path('eliminaAlbum/<int:id>',views.eliminarAlbum)
#]
from django.urls import path
from ArtistaAPI.views import (
    ArtistaListCreateView, ArtistaDetailView,
    MusicaListCreateView, MusicaDetailView,
    AlbumListCreateView, AlbumDetailView
)

urlpatterns = [

    path('artistas/', ArtistaListCreateView.as_view(), name='artista-list-create'),
    path('artistas/<int:pk>/', ArtistaDetailView.as_view(), name='artista-detail'),


    path('musicas/', MusicaListCreateView.as_view(), name='musica-list-create'),
    path('musicas/<int:pk>/', MusicaDetailView.as_view(), name='musica-detail'),


    path('albumes/', AlbumListCreateView.as_view(), name='album-list-create'),
    path('albumes/<int:pk>/', AlbumDetailView.as_view(), name='album-detail'),
]

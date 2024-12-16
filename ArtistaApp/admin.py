from django.contrib import admin
from ArtistaApp.models import Artista, Musica, Album

class ArtistaAdmin(admin.ModelAdmin):
    list_display = ['nombre_artista', 'nacionalidad', 'fechanacimiento', 'cancionescreada', 'aniosactivo']

class MusicaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'distribuidora', 'nombre_artista', 'duracion', 'num_reproducciones', 'fecha_lanzamiento']
    search_fields = ['nombre', 'nombre_artista__nombre_artista']

class AlbumAdmin(admin.ModelAdmin):
    list_display = ['titulo_album', 'fecha_lanzamiento', 'genero_album', 'discografica', 'numero_de_canciones', 'nombre']
    list_filter = ['genero_album', 'fecha_lanzamiento']

admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Musica, MusicaAdmin)
admin.site.register(Album, AlbumAdmin)

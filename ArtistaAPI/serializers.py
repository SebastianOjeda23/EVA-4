from rest_framework import serializers
from ArtistaAPI.models import Artista, Musica, Album

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = '__all__'  

class MusicaSerializer(serializers.ModelSerializer):
    # Cambié el campo 'nombre_artista' para que reciba solo el ID del artista
    nombre_artista = serializers.PrimaryKeyRelatedField(queryset=Artista.objects.all())

    class Meta:
        model = Musica
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    # Si fuera necesario un campo relacionado con música, se seguiría la misma lógica
    nombre = MusicaSerializer()

    class Meta:
        model = Album
        fields = '__all__'

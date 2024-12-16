from django import forms
from ArtistaApp.models import Artista, Musica, Album

class FormArtista(forms.ModelForm):
    class Meta:
        model = Artista
        fields = '__all__'

    def clean_cancionescreada(self):
        cancionescreada = self.cleaned_data.get('cancionescreada')
        if cancionescreada < 0:
            raise forms.ValidationError("El número de canciones creadas no puede ser negativo.")
        return cancionescreada
    
    def clean_aniosactivo(self):
        aniosactivo = self.cleaned_data.get('aniosactivo')
        if aniosactivo < 0:
            raise forms.ValidationError("El número de años activo no puede ser negativo.")
        return aniosactivo

class FormMusica(forms.ModelForm):
    class Meta:
        model = Musica
        fields = '__all__'

    def clean_duracion(self):
        duracion = self.cleaned_data.get('duracion')
        if duracion <= 0:
            raise forms.ValidationError("La duración debe ser un número positivo.")
        return duracion
    
    def clean_num_reproducciones(self):
        num_reproducciones = self.cleaned_data.get('num_reproducciones')
        if num_reproducciones < 0:
            raise forms.ValidationError("El número de reproducciones no puede ser negativo.")
        return num_reproducciones

class FormAlbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

    def clean_numero_de_canciones(self):
        numero_de_canciones = self.cleaned_data.get('numero_de_canciones')
        if numero_de_canciones <= 0:
            raise forms.ValidationError("El número de canciones debe ser mayor a cero.")
        return numero_de_canciones

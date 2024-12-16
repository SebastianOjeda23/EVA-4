from django.db import models

class Artista(models.Model):
    nombre_artista = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=100)
    fechanacimiento = models.DateField()
    cancionescreada = models.IntegerField()
    aniosactivo = models.IntegerField()

    def __str__(self):
        return self.nombre_artista

class Musica(models.Model):
    nombre = models.CharField(max_length=100)
    distribuidora = models.CharField(max_length=50)
    nombre_artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    duracion = models.IntegerField()
    num_reproducciones = models.IntegerField()
    fecha_lanzamiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} - {self.nombre_artista}"

class Album(models.Model):
    titulo_album = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField()
    genero_album = models.CharField(max_length=50)
    discografica = models.CharField(max_length=100)
    numero_de_canciones = models.IntegerField()
    nombre = models.ForeignKey(Musica, on_delete=models.CASCADE, related_name='albumes')

    def __str__(self):
        return f"{self.titulo_album} - {self.genero_album}"

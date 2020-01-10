from django.db import models
from datetime import date

class Musico(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(default=date.today)
    instrumento = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_fundacion = models.DateField(default=date.today)
    estilo_musical = models.CharField(max_length=100)
    componentes = models.ManyToManyField(Musico)

    def __str__(self):
        return self.nombre

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    distribuidora = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField(default=date.today)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
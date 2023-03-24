from django.db import models

# Create your models here.

class Cantante(models.Model):
    nombre = models.CharField(max_length=20)
    anio_de_nacimiento = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.anio_de_nacimiento}'
    

class Cancion(models.Model):
    nombre = models.CharField(max_length=20)
    autor = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.autor}'
    

class Album(models.Model):
    nombre = models.CharField(max_length=20)
    autor = models.CharField(max_length=20)
    anio_de_lanzamiento = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.autor} - ANIO DE LANZAMIENTO:{self.anio_de_lanzamiento}'
    

class Bandaa(models.Model):
    nombre = models.CharField(max_length=20)
    mejor_disco = models.CharField(max_length=20)
    anio = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.mejor_disco} - {self.anio}'

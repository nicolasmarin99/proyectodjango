from django.db import models


class Juego(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.ImageField(upload_to='juegos/')
    descripcion = models.TextField()
    cantidad = models.IntegerField(default=0)


def __str__(self):
    return self.nombre

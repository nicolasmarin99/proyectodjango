from django.db import models
from django.db import models
from juegos.models import Juego


class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

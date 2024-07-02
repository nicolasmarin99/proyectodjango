from django.shortcuts import render

from django.shortcuts import render, redirect
from juegos.models import Juego


def agregar_al_carrito(request, juego_id):


juego = Juego.objects.get(id=juego_id)
carrito = request.session.get('carrito', {})
carrito[juego_id] = carrito.get(juego_id, 0) + 1
request.session['carrito'] = carrito
return redirect('ver_carrito')


def ver_carrito(request):


carrito = request.session.get('carrito', {})
items = []
total = 0
for juego_id, cantidad in carrito.items():
juego = Juego.objects.get(id=juego_id)
subtotal = juego.precio * cantidad
total += subtotal
items.append({'juego': juego, 'cantidad': cantidad, 'subtotal': subtotal})
return render(request, 'carrito/ver_carrito.html', {'items': items, 'total': total})

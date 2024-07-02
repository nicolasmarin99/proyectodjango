from juegos.models import Juego
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .forms import JuegoForm


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Email o contraseña incorrectos'})


def detalle_juego(request, juego_id):
    juego = Juego.objects.get(id=juego_id)
    return render(request, 'juegos/detalle_juego.html', {'juego': juego})


def lista_juegos(request):
    juegos = Juego.objects.all()
    return render(request, 'juegos/lista_juegos.html', {'juegos': juegos})


@login_required
def agregar_juego(request):
def agregar_juego(request):


if request.method == 'POST':
form = JuegoForm(request.POST, request.FILES)
if form.is_valid():
form.save()
return redirect('lista_juegos')
else:
form = JuegoForm()
return render(request, 'juegos/agregar_juego.html', {'form': form})

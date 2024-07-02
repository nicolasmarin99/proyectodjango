from . import views
from django.urls import path

urlpatterns = [
    path('', views.lista_juegos, name='lista_juegos'),
    path('<int:juego_id>/', views.detalle_juego, name='detalle_juego'),

]

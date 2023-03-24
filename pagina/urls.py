from django.urls import path
from pagina.views import *

urlpatterns = [
    path('', buscar_banda, name = 'buscar_bandas'),
    path('bandas/', bandas, name = 'Bandas'),
    path('canciones/', canciones, name = 'Canciones'),
    path('albumes/', albumes, name = 'Albumes'),
    path('cantantes/', cantantes, name = 'Cantantes'),
]
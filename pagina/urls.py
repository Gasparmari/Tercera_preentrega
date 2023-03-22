from django.urls import path
from pagina.views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('entregables/', entregables, name = 'Entregables'),
    path('cursos/', cursos, name = 'Cursos'),
    path('profesores/', profesores, name = 'Profesores'),
    path('estudiantes/', estudiantes, name = 'Estudiantes')
]
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'pagina/index.html')

def profesores(request):
    return render(request, 'pagina/profesores.html')

def estudiantes(request):
    return render(request, 'pagina/estudiantes.html')

def entregables(request):
    return render(request, 'pagina/entregables.html')

def cursos(request):
    return render(request, 'pagina/cursos.html')
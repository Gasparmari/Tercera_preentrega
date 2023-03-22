from django.contrib import admin
from pagina.models import Profesore, Entregable, Estudiante, Curso

# Register your models here.

admin.site.register(Curso)

admin.site.register(Profesore)

admin.site.register(Entregable)

admin.site.register(Estudiante)
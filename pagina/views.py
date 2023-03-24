from django.shortcuts import render
from pagina.models import Cantante, Cancion, Album, Bandaa
from pagina.forms import BandasForm, BuscarbandaForm
# from pagina.models import Cantante

# Create your views here.


def buscar_banda(request):
    if request.method == "POST":

                bandas = Bandaa.objects.filter(nombre=(request.POST['banda']))

                return render(request, "pagina/buscar_bandas.html", {"data": [bandas]})
    else:
        miFormulario = BuscarbandaForm()

    return render(request, 'pagina/buscar_bandas.html' , {'miFormulario': miFormulario})



def bandas(request):
    if request.method == "POST":

            miFormulario = BandasForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                banda = Bandaa(nombre=informacion["nombre"], mejor_disco=informacion["mejor_disco"], anio=informacion["anio"])
                banda.save()
                return render(request, "pagina/index.html")
    else:
        miFormulario = BandasForm()


    return render(request, 'pagina/bandas.html', {'miFormulario': miFormulario})



def canciones(request):

    if request.method == "POST":

        nombre = request.POST["cancion"]
        autor = request.POST["autor"]
        Canciones = Cancion(nombre=nombre, autor=autor)
        Canciones.save()

    return render(request, 'pagina/canciones.html', {'pag': "canciones"})



def albumes(request):

    if request.method == "POST":

        nombre = request.POST["album"]
        autor = request.POST["autor"]
        anio = request.POST["lanzamiento"]
        album = Album(nombre=nombre, autor=autor, anio_de_lanzamiento=anio)
        album.save()

    return render(request, 'pagina/albumes.html', {'pag': "albumes"})



def cantantes(request):

    if request.method == "POST":

        nombre = request.POST["cantante"]
        anio = request.POST["anio"]
        cantante = Cantante(nombre=nombre, anio_de_nacimiento=anio)
        cantante.save()

    return render(request, 'pagina/cantantes.html')


#     if request.method == "POST":
#         print(f'\n\n{request.POST}\n\n')
#         nombre = request.POST["cantante"]
#         anio = request.POST["anio"]
        
#     return render(request, 'pagina/cantantes.html')
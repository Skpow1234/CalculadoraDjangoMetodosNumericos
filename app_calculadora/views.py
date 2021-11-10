from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def vista_inicio(request):
    diccionario = {
        'titulo' : "Inicio",
        'paginaPrincipal' : "Inicio",
    }
    return render(request, 'inicio/inicio.html', context=diccionario)


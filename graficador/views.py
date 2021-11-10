from django.shortcuts import render
from static.lib.Calculadora import *
import matplotlib.pyplot as plt
from math import *

# Create your views here.
objCalculadora = Calculadora()

def vista_graficador(request):
    titulo = "Graficador"
    paginaPrincipal = "Graficador"
    diccionario = {
        'titulo' : titulo,
        'paginaPrincipal' : paginaPrincipal
    }
    return render(request, 'graficador/graficador.html', context=diccionario)

def mostrar_grafico(request):
    funcion = request.POST['entrada-funcion']
    diccionario = {}
    try :
        Calculadora.generar_grafico(funcion, -10, 10, 7.25, 5)
        diccionario = {
            'titulo' : "Graficador",
            'paginaPrincipal' : "Graficador",
            'existeResultado' : True,
            'existeTabla' : False,
            'existeGrafico': False,
            'existeTeoria': False,
            'resultado': True, 
            'funcion': funcion,
        }
        return render(request, 'graficador/graficador.html', context=diccionario)
    except:
        return vista_graficador(request)



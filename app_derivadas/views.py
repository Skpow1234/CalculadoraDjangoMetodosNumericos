from django.shortcuts import render
from static.lib.Calculadora import *
from static.lib.Utilidad import *
from math import *

# Create your views here.
objCalculadora = Calculadora()

def vista_derivadas(request):
    titulo = "Derivadas"
    paginaPrincipal = "Derivadas"
    diccionario = {
        'titulo': titulo,
        'paginaPrincipal': paginaPrincipal
    }
    return render(request, 'derivadas/derivadas.html', context=diccionario)

def vista_derivada_numerica(request):
    titulo = "Derivada numerica"
    paginaPrincipal = "Derivadas"
    paginaSecundaria = "Derivada numerica"
    diccionario = {
        'titulo': titulo,
        'paginaPrincipal': paginaPrincipal,
        'paginaSecundaria': paginaSecundaria
    }
    return render(request, 'derivadas/derivada_numerica.html', context=diccionario)

def vista_derivada_simbolica(request):
    titulo = "Derivada simbolica"
    paginaPrincipal = "Derivadas"
    paginaSecundaria = "Derivada simbolica"
    diccionario = {
        'titulo': titulo,
        'paginaPrincipal': paginaPrincipal,
        'paginaSecundaria': paginaSecundaria
    }
    return render(request, 'derivadas/derivada_simbolica.html', context=diccionario)

#CALCULO
def mostrar_calculo_derivada_numerica(request):
    print("SOY POST:", request.POST)
    funcion = request.POST['entrada-funcion']
    ordenDerivada = request.POST['entrada-orden-derivada']
    numero = request.POST['entrada-numero']
    try:
        resultado = objCalculadora.calcular_derivada_numerica(funcion, float(numero), int(ordenDerivada))
        if resultado != None:
            existeResultado = True
            Calculadora.generar_grafico(objCalculadora.calcular_derivada_simbolica(funcion, int(ordenDerivada)))
        else:
            existeResultado = False
        diccionario = {
            'titulo' : "Derivada Numerica",
            'paginaPrincipal' : "Derivadas",
            'paginaSecundaria' : "Derivada Numerica",
            'existeResultado' : existeResultado,
            'existeTabla' : False,
            'existeGrafico': True,
            'existeTeoria': True,
            'resultado': resultado,
            'funcion': funcion,
            'ordenDerivada': ordenDerivada,
            'numero': numero
        }
        return render(request, 'derivadas/derivada_numerica.html', context=diccionario)
    except:
        return vista_derivada_numerica(request)

def mostrar_calculo_derivada_simbolica(request):
    funcion = request.POST['entrada-funcion']
    ordenDerivada = request.POST['entrada-orden-derivada']
    try:
        resultado = objCalculadora.calcular_derivada_simbolica(funcion, int(ordenDerivada))
        if resultado != None:
            existeResultado = True
            Calculadora.generar_grafico(resultado)
        else:
            existeResultado = False
        diccionario = {
            'titulo' : "Derivada Simbolica",
            'paginaPrincipal' : "Derivadas",
            'paginaSecundaria' : "Derivada Simbolica",
            'existeResultado' : existeResultado,
            'existeTabla' : False,
            'existeGrafico': True,
            'existeTeoria': True,
            'resultado': Utilidad.quitar_espacios(Utilidad.regular_expresion(resultado)),
            'funcion': funcion,
            'ordenDerivada': ordenDerivada,
        }
        return render(request, 'derivadas/derivada_simbolica.html', context=diccionario)
    except:
        return vista_derivada_simbolica(request)
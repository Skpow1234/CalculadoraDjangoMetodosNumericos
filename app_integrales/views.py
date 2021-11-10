from os import name
from django.shortcuts import render
from static.lib.Calculadora import *
from static.lib.Utilidad import *

# Create your views here.
objCalculadora = Calculadora()

def vista_integrales(request):
    diccionario = {
        'titulo': "Integrales",
        'paginaPrincipal': "Integrales"
    }
    return render(request, 'integrales/integrales.html', context=diccionario)

def vista_integracion_numerica_rectangulos(request):
    diccionario = {
        'titulo': "Integracion por rectangulos",
        'paginaPrincipal': "Integrales",
        'paginaSecundaria': "Integracion por rectangulos"
    }
    return render(request, 'integrales/rectangulos.html', context=diccionario)

def vista_integracion_numerica_trapecios(request):
    diccionario = {
        'titulo': "Integracion por trapecios",
        'paginaPrincipal': "Integrales",
        'paginaSecundaria': "Integracion por trapecios"
    }
    return render(request, 'integrales/trapecios.html', context=diccionario)

def vista_integracion_numerica_simpson1_3(request):
    diccionario = {
        'titulo': "Integracion por Simpson 1/3",
        'paginaPrincipal': "Integrales",
        'paginaSecundaria': "Integracion por Simpson 1/3"
    }
    return render(request, 'integrales/simpson1_3.html', context=diccionario)

def vista_integracion_numerica_simpson3_8(request):
    diccionario = {
        'titulo': "Integracion por Simpson 3/8",
        'paginaPrincipal': "Integrales",
        'paginaSecundaria': "Integracion por Simpson 3/8"
    }
    return render(request, 'integrales/simpson3_8.html', context=diccionario)

def vista_integracion_numerica_montecarlo(request):
    diccionario = {
        'titulo': "Integracion por Montecarlo",
        'paginaPrincipal': "Integrales",
        'paginaSecundaria': "Integracion por Montecarlo"
    }
    return render(request, 'integrales/montecarlo.html', context=diccionario)

#CALCULO
def mostrar_calculo_integracion_numerica_rectangulos(request):
    funcion = request.POST['entrada-funcion']
    extremoIzquierdo = float(request.POST['entrada-extremo-izquierdo'])
    extremoDerecho = float(request.POST['entrada-extremo-derecho'])
    cantidadDivisiones = int(request.POST['entrada-cantidad-divisiones'])
    
    resultado = {
        'Extremo izquierdo': objCalculadora.calcular_integral_numerica("izq", funcion, extremoIzquierdo, extremoDerecho, cantidadDivisiones),
        'Punto medio': objCalculadora.calcular_integral_numerica("med", funcion, extremoIzquierdo, extremoDerecho, cantidadDivisiones),
        'Extremo derecho': objCalculadora.calcular_integral_numerica("der", funcion, extremoIzquierdo, extremoDerecho, cantidadDivisiones)
    }
    if resultado != None:
        existeResultado = True
        Calculadora.generar_grafico(funcion, extremoIzquierdo, extremoDerecho)
    else:
        existeResultado = False
    diccionario = {
        'titulo': "Integracion por rectangulos",
        'paginaPrincipal': "Integrales",
        'paginaSecundaria': "Integracion por rectangulos",
        'existeResultado': existeResultado,
        'existeTabla': False,
        'existeGrafico': True,
        'existeTeoria': True,
        'resultado': resultado, 
        'funcion': funcion,
        'extremoIzquierdo': extremoIzquierdo,
        'extremoDerecho': extremoDerecho,
        'cantidadDivisiones': cantidadDivisiones
    }
    return render(request, 'integrales/rectangulos.html', context=diccionario)

def mostrar_calculo_integracion_numerica_trapecios(request):
    funcion = request.POST['entrada-funcion']
    extremoIzquierdo = float(request.POST['entrada-extremo-izquierdo'])
    extremoDerecho = float(request.POST['entrada-extremo-derecho'])
    cantidadDivisiones = int(request.POST['entrada-cantidad-divisiones'])
    
    resultado = objCalculadora.calcular_integral_numerica("trapecios", funcion, extremoIzquierdo, extremoDerecho, cantidadDivisiones)
    if resultado != None:
        existeResultado = True
        Calculadora.generar_grafico(funcion, extremoIzquierdo, extremoDerecho)
    else:
        existeResultado = False
    diccionario = {
        'titulo': "Integracion por trapecios",
        'paginaPrincipal': "Integrales",
        'paginaSecundaria': "Integracion por trapecios",
        'existeResultado': existeResultado,
        'existeTabla': False,
        'existeGrafico': True,
        'existeTeoria': True,
        'resultado': resultado,
        'funcion': funcion,
        'extremoIzquierdo': extremoIzquierdo,
        'extremoDerecho': extremoDerecho,
        'cantidadDivisiones': cantidadDivisiones
    }
    return render(request, 'integrales/trapecios.html', context=diccionario)

def mostrar_calculo_integracion_numerica_simpson1_3(request):
    funcion = request.POST['entrada-funcion']
    extremoIzquierdo = float(request.POST['entrada-extremo-izquierdo'])
    extremoDerecho = float(request.POST['entrada-extremo-derecho'])
    cantidadDivisiones = int(request.POST['entrada-cantidad-divisiones'])

    resultado = objCalculadora.calcular_integral_numerica("simpson 1/3", funcion, extremoIzquierdo, extremoDerecho, cantidadDivisiones)
    if resultado != None:
        existeResultado = True
        Calculadora.generar_grafico(funcion, extremoIzquierdo, extremoDerecho)
    else:
        existeResultado = False
    diccionario = {
        'titulo': "Integracion por Simpson 1/3",
        'paginaPrincipal': "Integrales",
        'paginaSecundaria': "Integracion por Simpson 1/3",
        'existeResultado': existeResultado,
        'existeTabla': False,
        'existeGrafico': True,
        'existeTeoria': True,
        'resultado': resultado,
        'funcion': funcion,
        'extremoIzquierdo': extremoIzquierdo,
        'extremoDerecho': extremoDerecho,
        'cantidadDivisiones': cantidadDivisiones
    }
    return render(request, 'integrales/simpson1_3.html', context=diccionario)

def mostrar_calculo_integracion_numerica_simpson3_8(request):
    funcion = request.POST['entrada-funcion']
    extremoIzquierdo = float(request.POST['entrada-extremo-izquierdo'])
    extremoDerecho = float(request.POST['entrada-extremo-derecho'])
    cantidadDivisiones = int(request.POST['entrada-cantidad-divisiones'])

    resultado = objCalculadora.calcular_integral_numerica("simpson 3/8", funcion, extremoIzquierdo, extremoDerecho, cantidadDivisiones)
    if resultado != None:
        existeResultado = True
        Calculadora.generar_grafico(funcion, extremoIzquierdo, extremoDerecho)
    else:
        existeResultado = False
    diccionario = {
        'titulo': "Integracion por Simpson 3/8",
        'paginaPrincipal': "Integrales",
        'paginaSecundaria': "Integracion por Simpson 3/8",
        'existeResultado': existeResultado,
        'existeTabla': False,
        'existeGrafico': True,
        'existeTeoria': True,
        'resultado': resultado,
        'funcion': funcion,
        'extremoIzquierdo': extremoIzquierdo,
        'extremoDerecho': extremoDerecho,
        'cantidadDivisiones': cantidadDivisiones
    }
    return render(request, 'integrales/simpson3_8.html', context=diccionario)

def mostrar_calculo_integracion_numerica_montecarlo(request):
    funcion = request.POST['entrada-funcion']
    extremoIzquierdo = float(request.POST['entrada-extremo-izquierdo'])
    extremoDerecho = float(request.POST['entrada-extremo-derecho'])
    cantidadPuntos = int(request.POST['entrada-cantidad-puntos'])

    resultado = objCalculadora.calcular_integral_numerica("montecarlo", funcion, extremoIzquierdo, extremoDerecho, cantidadPuntos)
    if resultado != None:
        existeResultado = True
        Calculadora.generar_grafico(funcion, extremoIzquierdo, extremoDerecho)
    else:
        existeResultado = False
    diccionario = {
        'titulo': "Integracion por Montecarlo",
        'paginaPrincipal': "Integrales",
        'paginaSecundaria': "Integracion por Montecarlo",
        'existeResultado': existeResultado,
        'existeTabla': False,
        'existeGrafico': True,
        'existeTeoria': True,
        'resultado': resultado,
        'funcion': funcion,
        'extremoIzquierdo': extremoIzquierdo,
        'extremoDerecho': extremoDerecho,
        'cantidadPuntos': cantidadPuntos
    }
    return render(request, 'integrales/montecarlo.html', context=diccionario)
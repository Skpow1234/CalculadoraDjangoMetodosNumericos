from django.shortcuts import render
from static.lib.Calculadora import *
from static.lib.Utilidad import *

objCalculadora = Calculadora()

def vista_raices(request):
    titulo = "Raices"
    paginaPrincipal = "Raices"
    diccionario = {
        'titulo' : titulo,
        'paginaPrincipal' : paginaPrincipal
    }
    return render(request, 'raices/raices.html', context=diccionario)

def vista_raices_biseccion(request):
    titulo = "Biseccion"
    paginaPrincipal = "Raices"
    paginaSecundaria = "Biseccion"
    diccionario = {
        'titulo' : titulo,
        'paginaPrincipal' : paginaPrincipal,
        'paginaSecundaria' : paginaSecundaria
    }
    return render(request, 'raices/biseccion.html', context=diccionario)

def vista_raices_falsa_posicion(request):
    titulo = "Falsa posicion"
    paginaPrincipal = "Raices"
    paginaSecundaria = "Falsa posicion"
    diccionario = {
        'titulo' : titulo,
        'paginaPrincipal' : paginaPrincipal,
        'paginaSecundaria' : paginaSecundaria
    }
    return render(request, 'raices/falsa_posicion.html', context=diccionario)

def vista_raices_newthon_raphson(request):
    titulo = "Newton Raphson"
    paginaPrincipal = "Raices"
    paginaSecundaria = "Newton Raphson"
    diccionario = {
        'titulo' : titulo,
        'paginaPrincipal' : paginaPrincipal,
        'paginaSecundaria' : paginaSecundaria
    }
    return render(request, 'raices/newton_raphson.html', context=diccionario)

def vista_raices_secante(request):
    titulo = "Secante"
    paginaPrincipal = "Raices"
    paginaSecundaria = "Secante"
    diccionario = {
        'titulo' : titulo,
        'paginaPrincipal' : paginaPrincipal,
        'paginaSecundaria' : paginaSecundaria
    }
    return render(request, 'raices/secante.html', context=diccionario)

def vista_raices_polinomio(request):
    titulo = "Polinomio"
    paginaPrincipal = "Raices"
    paginaSecundaria = "Polinomio"
    diccionario = {
        'titulo' : titulo,
        'paginaPrincipal' : paginaPrincipal,
        'paginaSecundaria' : paginaSecundaria
    }
    return render(request, 'raices/polinomio.html', context=diccionario)

#CALCULOS
def mostrar_calculo_biseccion(request):
    funcion = request.POST['entrada-funcion']
    limiteInferior = request.POST['entrada-limite-inferior']
    limiteSuperior = request.POST['entrada-limite-superior']
    errorTolerado = request.POST['entrada-error-tolerado']
    diccionario = {}
    try :
        tabla = objCalculadora.calcular_raices("biseccion", funcion, float(limiteInferior), float(limiteSuperior), float(errorTolerado))
        if tabla != None:
            existeResultado = True
            Calculadora.generar_grafico(funcion, -2*tabla[-1][1], 2*tabla[-1][1])
        else:
            existeResultado = False
        diccionario = {
            'titulo' : "Biseccion",
            'paginaPrincipal' : "Raices",
            'paginaSecundaria' : "Biseccion",
            'existeResultado' : existeResultado,
            'existeTabla' : True,
            'existeGrafico': True,
            'existeTeoria': True,
            'funcion' : funcion,
            'limiteInferior' : limiteInferior,
            'limiteSuperior' : limiteSuperior,
            'errorTolerado' : errorTolerado,
            'raizResultado' : tabla[-1][5],
            'errorResultado' : tabla[-1][-1],
            'tablaResultado' : tabla,
            'direccionGrafico': "\img\grafico.png"
        }
        return render(request, 'raices/biseccion.html', context=diccionario)
    except:
        return vista_raices_biseccion(request)

def mostrar_calculo_falsa_posicion(request):
    funcion = request.POST['entrada-funcion']
    limiteInferior = request.POST['entrada-limite-inferior']
    limiteSuperior = request.POST['entrada-limite-superior']
    errorTolerado = request.POST['entrada-error-tolerado']
    diccionario = {}
    try :
        tabla = objCalculadora.calcular_raices("regla falsa", funcion, float(limiteInferior), float(limiteSuperior), float(errorTolerado))
        if tabla != None:
            existeResultado = True
            Calculadora.generar_grafico(funcion, -2*tabla[-1][1], 2*tabla[-1][1])
        else:
            existeResultado = False
        diccionario = {
            'titulo' : "Falsa Posicion",
            'paginaPrincipal' : "Raices",
            'paginaSecundaria' : "Falsa Posicion",
            'existeResultado' : existeResultado,
            'existeTabla' : True,
            'existeGrafico': True,
            'existeTeoria': True,
            'funcion' : funcion,
            'limiteInferior' : limiteInferior,
            'limiteSuperior' : limiteSuperior,
            'errorTolerado' : errorTolerado,
            'raizResultado' : tabla[-1][5],
            'errorResultado' : tabla[-1][-1],
            'tablaResultado' : tabla
        }
        return render(request, 'raices/falsa_posicion.html', context=diccionario)
    except:
        return vista_raices_falsa_posicion(request)

def mostrar_calculo_newthon_raphson(request):
    funcion = request.POST['entrada-funcion']
    puntoInicial = request.POST['entrada-punto-inicial']
    errorTolerado = request.POST['entrada-error-tolerado']
    diccionario = {}
    try :
        tabla = objCalculadora.calcular_raices("newton raphson", funcion, float(puntoInicial), float(0), float(errorTolerado))
        if tabla != None:
            existeResultado = True
            Calculadora.generar_grafico(funcion, -2*tabla[-1][1], 2*tabla[-1][1])
        else:
            existeResultado = False
        diccionario = {
            'titulo' : "Newton Raphson",
            'paginaPrincipal' : "Raices",
            'paginaSecundaria' : "Newton Raphson",
            'existeResultado' : existeResultado,
            'existeTabla' : True,
            'existeGrafico': True,
            'existeTeoria': True,
            'funcion' : funcion,
            'puntoInicial' : puntoInicial,
            'errorTolerado' : errorTolerado,
            'raizResultado' : tabla[-1][1],
            'errorResultado' : tabla[-1][-1],
            'tablaResultado' : tabla
        }
        return render(request, 'raices/newton_raphson.html', context=diccionario)
    except:
        return vista_raices_newthon_raphson(request)


def mostrar_calculo_secante(request):
    funcion = request.POST['entrada-funcion']
    limiteInferior = request.POST['entrada-limite-inferior']
    limiteSuperior = request.POST['entrada-limite-superior']
    errorTolerado = request.POST['entrada-error-tolerado']
    diccionario = {}
    try :
        tabla = objCalculadora.calcular_raices("secante", funcion, float(limiteInferior), float(limiteSuperior), float(errorTolerado))
        if tabla != None:
            existeResultado = True
            Calculadora.generar_grafico(funcion, -2*tabla[-1][1], 2*tabla[-1][1])
        else:
            existeResultado = False
        diccionario = {
            'titulo' : "Secante",
            'paginaPrincipal' : "Raices",
            'paginaSecundaria' : "Secante",
            'existeResultado' : existeResultado,
            'existeTabla' : True,
            'existeGrafico': True,
            'existeTeoria': True,
            'funcion' : funcion,
            'limiteInferior' : limiteInferior,
            'limiteSuperior' : limiteSuperior,
            'errorTolerado' : errorTolerado,
            'raizResultado' : tabla[-1][5],
            'errorResultado' : tabla[-1][-1],
            'tablaResultado' : tabla
        }
        return render(request, 'raices/secante.html', context=diccionario)
    except:
        return vista_raices_secante(request)

def mostrar_calculo_polinomio(request):
    funcion = request.POST['entrada-funcion']
    diccionario = {}
    try :
        tabla = objCalculadora.calcular_raices("polinomio", funcion, float(0), float(0), float(0))
        if tabla != None:
            existeResultado = True
            Calculadora.generar_grafico(funcion)
        else:
            existeResultado = False
        diccionario = {
            'titulo' : "Polinomio",
            'paginaPrincipal' : "Raices",
            'paginaSecundaria' : "Polinomio",
            'existeResultado' : existeResultado,
            'existeTabla' : False,
            'existeGrafico': True,
            'existeTeoria': True,
            'funcion': funcion,
            'tablaResultado': tabla
        }
        return render(request, 'raices/polinomio.html', context=diccionario)
    except:
        return vista_raices_polinomio(request)
# Create your views here.

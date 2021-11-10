from django.shortcuts import render
from static.lib.Utilidad import Utilidad

# Create your views here.
def vista_evaluador(request):
    titulo = "Evaluador"
    paginaPrincipal = "Evaluador"
    diccionario = {
        'titulo': titulo,
        'paginaPrincipal': paginaPrincipal,
        'teoria': False
    }
    return render(request, 'evaluador/evaluador.html', context=diccionario)

#CALCULO
def mostrar_calculo_evaluador(request):
    titulo = "Evaluador"
    paginaPrincipal = "Evaluador"
    funcion = request.POST['entrada-funcion']
    numero = request.POST['entrada-numero']
    resultado = False
    try:
        resultado = Utilidad.evaluar_expresion(float(numero), Utilidad.formatear_expresion(funcion))
        diccionario = {
            'titulo': titulo,
            'paginaPrincipal': paginaPrincipal,
            'teoria': False,
            'funcion': funcion,
            'numero': numero,
            'resultado': resultado
        }
        return render(request, 'evaluador/evaluador.html', context=diccionario)
    except:
        return vista_evaluador(request)

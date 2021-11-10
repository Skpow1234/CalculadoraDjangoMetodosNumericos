from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from static.lib.Calculadora import *
from static.lib.Utilidad import *
# Create your views here.
objCalculadora = Calculadora()

def vista_conversion(request):
    titulo = "Conversion"
    paginaPrincipal = "Conversion"
    diccionario = {
        'titulo' : titulo,
        'paginaPrincipal' : paginaPrincipal
    }
    return render(request, 'conversion/conversion.html', context=diccionario)

def vista_conversion_binario(request):
    diccionario = {
        'titulo' : "Sistema Binario",
        'paginaPrincipal' : "Conversion",
        'paginaSecundaria' : "Sistema Binario"
    }
    return render(request, 'conversion/binario.html', context=diccionario)

def vista_conversion_octal(request):
    titulo = "Octal"
    paginaPrincipal = "Conversion"
    paginaSecundaria = "Octal"
    diccionario = {
        'titulo' : titulo,
        'paginaPrincipal' : paginaPrincipal,
        'paginaSecundaria' : paginaSecundaria
    }
    return render(request, 'conversion/octal.html', context=diccionario)

def vista_conversion_decimal(request):
    titulo = "Decimal"
    paginaPrincipal = "Conversion"
    paginaSecundaria = "Decimal"
    diccionario = {
        'titulo' : titulo,
        'paginaPrincipal' : paginaPrincipal,
        'paginaSecundaria' : paginaSecundaria
    }
    return render(request, 'conversion/decimal.html', context=diccionario)

def vista_conversion_hexadecimal(request):
    titulo = "Hexadecimal"
    paginaPrincipal = "Conversion"
    paginaSecundaria = "Hexadecimal"
    diccionario = {
        'titulo' : titulo,
        'paginaPrincipal' : paginaPrincipal,
        'paginaSecundaria' : paginaSecundaria
    }
    return render(request, 'conversion/hexadecimal.html', context=diccionario)

def vista_conversion_hexadecimal(request):
    titulo = "Hexadecimal"
    paginaPrincipal = "Conversion"
    paginaSecundaria = "Hexadecimal"
    diccionario = {
        'titulo' : titulo,
        'paginaPrincipal' : paginaPrincipal,
        'paginaSecundaria' : paginaSecundaria
    }
    return render(request, 'conversion/hexadecimal.html', context=diccionario)

def vista_conversion_ieee754(request):
    titulo = "Estandar IEEE754"
    paginaPrincipal = "Conversion"
    paginaSecundaria = "Estandar IEEE754"
    diccionario = {
        'titulo' : titulo,
        'paginaPrincipal' : paginaPrincipal,
        'paginaSecundaria' : paginaSecundaria
    }
    return render(request, 'conversion/ieee754.html', context=diccionario)

#Calculos
def mostrar_calculo_binario(request):
    numero = request.POST['entrada-numero']
    try:
        diccionario = {
            'titulo' : "Sistema Binario",
            'paginaPrincipal' : "Conversion",
            'paginaSecundaria' : "Sistema Binario",
            'existeResultado' : True,
            'existeTabla' : False,
            'existeGrafico': False,
            'existeTeoria': True,
            'numero' : numero,
            'resultado' : {
                'Octal': objCalculadora.convertir_bases(numero, 2, 8),
                'Decimal': objCalculadora.convertir_bases(numero, 2, 10),
                'Hexadecimal': objCalculadora.convertir_bases(numero, 2, 16)
            } 
        }
        return render(request, 'conversion/binario.html', context=diccionario)
    except:
        return vista_conversion_binario(request)

def mostrar_calculo_octal(request):
    numero = request.POST['entrada-numero']
    try:
        diccionario = {
            'titulo' : "Sistema Octal",
            'paginaPrincipal' : "Conversion",
            'paginaSecundaria' : "Sistema Octal",
            'existeResultado' : True,
            'existeTabla' : False,
            'existeGrafico': False,
            'existeTeoria': True,
            'numero' : numero,
            'resultado' : {
                'Binario': objCalculadora.convertir_bases(numero, 8, 2),
                'Decimal': objCalculadora.convertir_bases(numero, 8, 10),
                'Hexadecimal': objCalculadora.convertir_bases(numero, 8, 16) #ERROR
            } 
        }
        return render(request, 'conversion/octal.html', context=diccionario)
    except:
        return vista_conversion_octal(request)

def mostrar_calculo_decimal(request):
    numero = request.POST['entrada-numero']
    try:
        diccionario = {
            'titulo' : "Sistema Decimal",
            'paginaPrincipal' : "Conversion",
            'paginaSecundaria' : "Sistema Decimal",
            'existeResultado' : True,
            'existeTabla' : False,
            'existeGrafico': False,
            'existeTeoria': True,
            'numero' : numero,
            'resultado' : {
                'Binario': objCalculadora.convertir_bases(numero, 10, 2),
                'Octal': objCalculadora.convertir_bases(numero, 10, 8),
                'Hexadecimal': objCalculadora.convertir_bases(numero, 10, 16)
            } 
        }
        return render(request, 'conversion/decimal.html', context=diccionario)
    except:
        return vista_conversion_decimal(request)

def mostrar_calculo_hexadecimal(request):
    numero = request.POST['entrada-numero']
    try:
        diccionario = {
            'titulo' : "Sistema Hexadecimal",
            'paginaPrincipal' : "Conversion",
            'paginaSecundaria' : "Sistema Hexadecimal",
            'existeResultado' : True,
            'existeTabla' : False,
            'existeGrafico': False,
            'existeTeoria': True,
            'numero' : numero,
            'resultado' : {
                'Binario': objCalculadora.convertir_bases(numero, 16, 2),
                'Octal': objCalculadora.convertir_bases(numero, 16, 8),
                'Decimal': objCalculadora.convertir_bases(numero, 16, 10)
            } 
        }
        return render(request, 'conversion/hexadecimal.html', context=diccionario)
    except:
        return vista_conversion_hexadecimal(request)

def mostrar_calculo_ieee754(request):
    numero = request.POST['entrada-numero']
    try:
        resultado32Bits = objCalculadora.convertir_bases(numero, 10, 75432)
        resultado64Bits = objCalculadora.convertir_bases(numero, 10, 75464)
        diccionario = {
            'titulo' : "Estandar IEEE754",
            'paginaPrincipal' : "Conversion",
            'paginaSecundaria' : "Estandar IEEE754",
            'existeResultado' : True,
            'existeTabla' : False,
            'existeGrafico': False,
            'existeTeoria': True,
            'numero' : numero,
            'resultado32Bits' : {
                'Signo': resultado32Bits[0],
                'Exponente': resultado32Bits[1],
                'Mantisa': resultado32Bits[2]
            },
            'resultado64Bits' : {
                'Signo': resultado64Bits[0],
                'Exponente': resultado64Bits[1],
                'Mantisa': resultado64Bits[2]
            } 
        }
        return render(request, 'conversion/ieee754.html', context=diccionario)
    except:
        return vista_conversion_ieee754(request)

def mostrar_calculo_ieee754_32Bits_a_decimal(request):
    signo = request.POST['Signo32Bits']
    exponente = request.POST['Exponente32Bits']
    mantisa = request.POST['Mantisa32Bits']
    try:
        numero = objCalculadora.ieee754_a_decimal(signo, exponente, mantisa, 32)
        resultado64Bits = objCalculadora.convertir_bases(numero, 10, 75464)
        diccionario = {
            'titulo' : "Estandar IEEE754",
            'paginaPrincipal' : "Conversion",
            'paginaSecundaria' : "Estandar IEEE754",
            'existeResultado' : True,
            'existeTabla' : False,
            'existeGrafico': False,
            'existeTeoria': True,
            'numero' : numero,
            'resultado32Bits' : {
                'Signo': signo,
                'Exponente': exponente,
                'Mantisa': mantisa
            },
            'resultado64Bits' : {
                'Signo': resultado64Bits[0],
                'Exponente': resultado64Bits[1],
                'Mantisa': resultado64Bits[2]
            } 
        }
        return render(request, 'conversion/ieee754.html', context=diccionario)
    except:
        return vista_conversion_ieee754(request)

def mostrar_calculo_ieee754_64Bits_a_decimal(request):
    signo = request.POST['Signo64Bits']
    exponente = request.POST['Exponente64Bits']
    mantisa = request.POST['Mantisa64Bits']
    try:
        numero = objCalculadora.ieee754_a_decimal(signo, exponente, mantisa, 64)
        resultado32Bits = objCalculadora.convertir_bases(numero, 10, 75432)
        diccionario = {
            'titulo' : "Estandar IEEE754",
            'paginaPrincipal' : "Conversion",
            'paginaSecundaria' : "Estandar IEEE754",
            'existeResultado' : True,
            'existeTabla' : False,
            'existeGrafico': False,
            'existeTeoria': True,
            'numero' : numero,
            'resultado32Bits' : {
                'Signo': resultado32Bits[0],
                'Exponente': resultado32Bits[1],
                'Mantisa': resultado32Bits[2]
            },
            'resultado64Bits' : {
                'Signo': signo,
                'Exponente': exponente,
                'Mantisa': mantisa
            }
        }
        return render(request, 'conversion/ieee754.html', context=diccionario)
    except:
        return vista_conversion_ieee754(request)
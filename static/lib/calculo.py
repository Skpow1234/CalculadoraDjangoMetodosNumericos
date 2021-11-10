from sympy import Symbol, diff
from math import *
import numpy as np
import sympy 

#UTILIDADES
def cambiar_formato_funcion(funcion):
    dato = funcion
    dato = dato.replace('ln', 'log')
    dato = dato.replace('sen', 'sin')
    dato = dato.replace('^', '**')
    return dato


#DECIMAL
def separar_entero_decimal(valor: str):
    numero = None
    try:
        numero = valor.split('.')
        return numero
    except:
        return None

def decimal_a(valor, base):
    numero = 0
    resultado = 0
    baseActual = 10
    baseNueva = 0
    parteEntera = 0
    parteDecimal = 0
    limiteDecimales = 12
    try:
        baseNueva = int(base)
        numero = separar_entero_decimal(str(float(valor)))
        parteEntera = parte_entera_base10(int(numero[0]), baseActual, baseNueva)
        resultado = parteEntera
        if len(numero) > 1 and numero[1] != "0":
            parteDecimal = parte_decimal_base10(float("0." + numero[1]), baseActual, baseNueva, limiteDecimales)
            if (limiteDecimales - len(parteDecimal)) > 0:
                while len(parteDecimal) < limiteDecimales:
                    parteDecimal = parteDecimal + "0"
            resultado = resultado + "." + parteDecimal
        return resultado
    except:
        return None

def parte_entera_base10(valor: int, baseActual, baseNueva):
    lista = []
    numero = 0
    iterador = 0
    resultado = 0
    diccionario = {
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F',
    }
    try:
        numero = valor
        while (numero / baseNueva) > 0:
            lista.append(int(numero % baseNueva))
            numero = int(numero / baseNueva)
        iterador = len(lista)
        if baseNueva != 16:
            while iterador > 0:
                resultado = resultado + lista[iterador - 1] * pow(baseActual, iterador - 1)
                iterador = iterador - 1
            resultado = str(resultado)[:len(str(resultado)) - 2]
        else:
            iterador = 0
            while iterador < len(lista):
                if lista[iterador] in diccionario.keys():
                    lista[iterador] = diccionario.get(lista[iterador])
                iterador = iterador + 1
            lista.reverse()
            resultado = "".join(map(str, lista))
        return resultado
    except:
        return None

def parte_decimal_base10(valor: float, baseActual, baseNueva, limiteDecimales):
    iterador = 0
    lista = []
    resultado = 0
    numero = 0
    iterador = 0
    diccionario = {
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F',
    }
    try:
        numero = valor
        while iterador < limiteDecimales:
            numero = numero * baseNueva
            lista.append(int(numero))
            numero = numero - lista[-1]
            iterador = iterador + 1
        iterador = 1
        if baseNueva != 16:
            while iterador <= limiteDecimales:
                resultado = resultado + lista[iterador - 1] * pow(baseActual, iterador * -1)
                iterador = iterador + 1
            resultado = str(round(resultado, limiteDecimales))[2:]
        else :
            iterador = 0
            while iterador < len(lista):
                if lista[iterador] in diccionario.keys():
                    lista[iterador] = diccionario.get(lista[iterador])
                iterador = iterador + 1
            resultado = "".join(map(str, lista))
        return resultado 
    except:
        return None

#BINARIO
def binario_a_decimal(valor):
    numero = []
    potencia = 0
    resultado =  0
    parteEntera = 0
    parteDecimal = 0
    limiteDecimales = 12
    iterador = 0
    try:
        numero = separar_entero_decimal(str(valor))
        parteEntera = list(map(int, numero[0]))
        potencia = len(parteEntera) - 1
        for i in parteEntera:
            resultado = resultado + (i * pow(2, potencia))
            potencia = potencia - 1
        if len(numero) > 1:
            parteDecimal = list(map(int, numero[1]))
            while iterador < limiteDecimales:
                if iterador < len(parteDecimal):
                    resultado = resultado + (parteDecimal[iterador] * pow(2, potencia))
                    potencia = potencia - 1
                iterador = iterador + 1
        return resultado
    except:
        return None

def binario_a_hexadecimal(valor):
    numero = ""
    parteEntera = ""
    parteDecimal = ""
    resultado = ""
    limiteDecimales = 12
    try:
        numero = separar_entero_decimal(str(valor))
        parteEntera = a_hexadecimal(numero[0])
        resultado = parteEntera
        if len(numero) > 1:
            parteDecimal = a_hexadecimal(numero[1])
            if (limiteDecimales - len(parteDecimal)) > 0:
                while len(parteDecimal) < limiteDecimales:
                    parteDecimal = parteDecimal + "0"
            resultado = resultado + "." + parteDecimal
        return resultado
    except:
        return None

def binario_a_octal(valor: str):
    numero = 0
    parteEntera = 0
    parteDecimal = 0
    resultado = 0
    limiteDecimales = 12
    try:
        numero = separar_entero_decimal(valor)
        parteEntera = a_octal(numero[0])
        resultado = parteEntera
        if len(numero) > 1:
            parteDecimal = a_octal(numero[1])
            if (limiteDecimales - len(parteDecimal)) > 0:
                while len(parteDecimal) < limiteDecimales:
                    parteDecimal = parteDecimal + "0"
            resultado = resultado + "." + parteDecimal
        return resultado
    except:
        return None

def a_hexadecimal(valor):
    numero = 0
    lista = []
    resultado = ""
    iterador = 0
    diccionario = {
        '0000' : '0',
        '0001' : '1',
        '0010' : '2',
        '0011' : '3',
        '0100' : '4',
        '0101' : '5',
        '0110' : '6',
        '0111' : '7',
        '1000' : '8',
        '1001' : '9',
        '1010' : 'A',
        '1011' : 'B',
        '1100' : 'C',
        '1101' : 'D',
        '1110' : 'E',
        '1111' : 'F',
    }
    try:
        numero = list(str(valor))
        numero.reverse()
        if len(numero) >= 4:
            while iterador < len(numero):
                if iterador % 4 == 0:
                    lista.append(list(map(str, numero[iterador:iterador + 4])))
                    lista[-1].reverse()
                iterador = iterador + 1
            if len(lista[-1]) < 4:
                iterador = 0
                while len(lista[-1]) < 4:
                    lista[-1].reverse()
                    lista[-1].append("0")
                    lista[-1].reverse()
            lista.reverse()
            for i in lista:
                resultado = resultado + diccionario["".join(i)]
        else:
            lista.append("".join(map(str, numero)))
            while iterador < (4 - len(numero)):
                lista[0] = lista[0] + '0'
                iterador = iterador + 1
            lista[0] = list(map(str, lista[0]))
            lista[0].reverse()
            lista[0] = "".join(lista[0])
            resultado = diccionario[lista[0]]
        return resultado
    except:
        return None

def a_octal(valor: str):
    numero = []
    lista = []
    resultado = ""
    iterador = 0
    diccionario = {
        '000' : '0',
        '001' : '1',
        '010' : '2',
        '011' : '3',
        '100' : '4',
        '101' : '5',
        '110' : '6',
        '111' : '7',
    }
    try:
        numero = list(str(valor))
        numero.reverse()
        if len(numero) >= 3:
            while iterador < len(numero):
                if iterador % 3 == 0:
                    lista.append(list(map(str, numero[iterador:iterador + 3])))
                    lista[-1].reverse()
                iterador = iterador + 1
            if len(lista[-1]) < 3:
                iterador = 0
                while len(lista[-1]) < 3:
                    lista[-1].reverse()
                    lista[-1].append("0")
                    lista[-1].reverse()
            lista.reverse()
            for i in lista:
                resultado = resultado + diccionario["".join(i)]
        else:
            lista.append("".join(map(str, numero)))
            while iterador < (3 - len(numero)):
                lista[0] = lista[0] + '0'
                iterador = iterador + 1
            lista[0] = list(map(str, lista[0]))
            lista[0].reverse()
            lista[0] = "".join(lista[0])
            resultado = diccionario[lista[0]]
        return resultado
    except:
        return None

#OCTAL
def octal_a(valor, base):
    numero = 0
    resultado = 0
    baseActual = 8
    baseNueva = 0
    parteEntera = 0
    parteDecimal = 0
    limiteDecimales = 12
    try:
        baseNueva = int(base)
        numero = float(valor)
        parteEntera, parteDecimal = separar_entero_decimal(str(numero))
        resultado = parte_entera_base8(int(parteEntera), baseActual, baseNueva)
        if int(parteDecimal) > 0:
            resultado = resultado + "." + parte_decimal_base8(float("0." + parteDecimal), baseActual, baseNueva, limiteDecimales)
        return resultado
    except:
        return None

def parte_entera_base8(valor, baseActual, baseNueva):
    lista = []
    numero = valor
    resultado = 0
    iterador = 0
    try:
        while (numero / baseNueva) > 0:
            lista.append(int(numero % baseNueva))
            numero = int(numero / baseNueva)
        iterador = len(lista)
        while iterador > 0:
            resultado = resultado + lista[iterador - 1] * pow(baseActual, iterador - 1)
            iterador = iterador - 1
        resultado = str(resultado)
        return resultado
    except:
        return None

def parte_decimal_base8(valor, baseActual, baseNueva, limiteDecimales):
    iterador = 0
    lista = []
    resultado = 0
    numero = valor
    iterador = 0
    try:
        while iterador < limiteDecimales:
            numero = numero * baseNueva
            lista.append(int(numero))
            numero = numero - lista[-1]
            iterador = iterador + 1
        iterador = 1
        while iterador < limiteDecimales:
            resultado = resultado + lista[iterador - 1] * pow(baseActual, iterador * -1)
            iterador = iterador + 1
        resultado = str(round(resultado, limiteDecimales + 1))[2:]
        return resultado 
    except:
        return None

def octal_a_binario(valor):
    numero = 0
    resultado = 0
    parteEntera = 0
    parteDecimal = 0
    limiteDecimales = 12
    try:
        numero = float(valor)
        numero = separar_entero_decimal(str(numero))
        parteEntera = a_binario(int(numero[0]))
        resultado = parteEntera
        if len(numero) > 0:
            parteDecimal = a_binario(int(numero[1]))
            if (limiteDecimales - len(parteDecimal)) > 0:
                while len(parteDecimal) < limiteDecimales:
                    parteDecimal = parteDecimal + "0"
        resultado = resultado + "." + parteDecimal
        return resultado
    except:
        return None

def a_binario(valor: int):
    numero = 0
    lista = []
    resultado = ""
    diccionario = {
        '0' : '000',
        '1' : '001',
        '2' : '010',
        '3' : '011',
        '4' : '100',
        '5' : '101',
        '6' : '110',
        '7' : '111',
    }
    try:
        numero = list(str(valor))
        for i in numero:
            if i in diccionario.keys():
                lista.append(diccionario[i])
        resultado = "".join(lista)
        return resultado
    except:
        return None

def octal_a_hexadecimal(valor):
    numero = 0
    resultado = 0
    parteEntera = 0
    parteDecimal = 0
    limiteDecimales = 0
    try:
        numero = separar_entero_decimal(str(float(valor)))
        parteEntera = binario_a_hexadecimal(a_binario(int(numero[0])))
        resultado = parteEntera
        if len(numero) > 1:
            parteDecimal = binario_a_hexadecimal(a_binario(int(numero[1])))
            if (limiteDecimales - len(parteDecimal)) > 0:
                while len(parteDecimal) < limiteDecimales:
                    parteDecimal = parteDecimal + "0"
        resultado = resultado + "." + parteDecimal
        return resultado
    except:
        return None 

#HEXADECIMAL
def hexadecimal_a_decimal(valor):
    numero = 0
    parteEntera = []
    parteDecimal = 0
    limiteDecimales = 12
    try:
        numero = separar_entero_decimal(str(valor))
        parteEntera = list(numero[0].upper())
        resultado = parte_entera_base16(parteEntera)
        if len(numero) > 1 and numero[1] != "0":
            parteDecimal = parte_decimal_base16(list(numero[1].upper()))
            if (limiteDecimales - len(parteDecimal)) > 0:
                while len(parteDecimal) < limiteDecimales:
                    parteDecimal = parteDecimal + "0"
            resultado = resultado + "." + parteDecimal
        return resultado
    except:
        return None

def parte_entera_base16(parteEntera):
    lista = []
    base = 16
    diccionario = {
        'A' : '10',
        'B' : '11',
        'C' : '12',
        'D' : '13',
        'E' : '14',
        'F' : '15',
    }
    potencia = 0
    resultado = 0
    try:
        for i in parteEntera:
            if i in diccionario.keys():
                lista.append(int(diccionario[i]))
            else:
                lista.append(int(i))
        potencia = len(lista) - 1
        for i in lista:
            resultado = resultado + (i * pow(base, potencia))
            potencia = potencia - 1
        return str(resultado)
    except:
        return None

def parte_decimal_base16(parteDecimal):
    lista = []
    base = 16
    diccionario = {
        'A' : '10',
        'B' : '11',
        'C' : '12',
        'D' : '13',
        'E' : '14',
        'F' : '15',
    }
    resultado = 0
    potencia = -1
    try:
        for i in parteDecimal:
            if i in diccionario.keys():
                lista.append(int(diccionario[i]))
            else:
                lista.append(int(i))
        for i in lista:
            resultado = resultado + (i * pow(base, potencia))
            potencia = potencia - 1
        return str(resultado)[2:]
    except:
        return None


def hexadecimal_a_octal(valor):
    return decimal_a(hexadecimal_a_decimal(valor), 8)

def hexadecimal_a_binario(valor):
    return decimal_a(hexadecimal_a_decimal(valor), 2)

#ESTANDAR IEEE
def mantisaestandarIEEE32bits(numero):
    mantisa=numero
    mantisa=mantisa.replace('-','')
    mantisa = mantisa.replace('.', '')
    lista=[x for x in mantisa]
    lista.pop(0)
    if(len(lista)<23):
        idx=len(lista)-1
        while idx<23:
            lista.append('0')
            idx=idx+1
    newMantisa=''
    index=0
    while index<23:
        newMantisa=newMantisa+lista[index]
        index=index+1
    return newMantisa

def signoestandarIEEE32bits(numero):
    signo = 0
    number = 0
    try:
        if number < 0:
            signo = 1
        return signo
    except:
        return None

def exponenteestandarIEEE32bits(numero):
    n=8
    exponente=0
    number = 0
    signo = 0
    try:
        number = float(numero)
        signo=signoestandarIEEE32bits(numero)
        if(signo==1):
            number=number*-1
        while int(number) != 1:
            number = number / 10
            exponente = exponente + 1
        exponente1 = exponente + ((pow(2, n - 1)) - 1)
        exponente1 = decimal_a(exponente1, 2)
        return exponente1
    except:
        return None

def mantisaestandarIEEE64bits(numero):
    mantisa=numero
    mantisa=mantisa.replace('-','')
    mantisa = mantisa.replace('.', '')
    lista=[x for x in mantisa]
    lista.pop(0)
    if(len(lista)<52):
        idx=len(lista)-1
        while idx<52:
            lista.append('0')
            idx=idx+1
    newMantisa=''
    index=0
    while index<52:
        newMantisa=newMantisa+lista[index]
        index=index+1

    return newMantisa

def signoestandarIEEE64bits(numero):
    signo = 0
    number = 0
    try:
        number = float(numero)
        if number < 0:
            signo = 1
        return signo
    except:
        return None

def exponenteestandarIEEE64bits(numero):
    n=11
    exponente=0
    number = 0
    signo=0
    try:
        number = float(numero)
        signo=signoestandarIEEE64bits(numero)
        if(signo==1):
            number=number*-1
        while int(number) != 1:
            number = number / 10
            exponente = exponente + 1
        exponente1 = exponente + ((pow(2, n - 1)) - 1)
        exponente1 = decimal_a(exponente1, 2)
        return exponente1
    except:
        return None

def estandarIEEE32Bits_a_decimal(signo: str,exponente: str,mantisa: str):
    final = -1
    if(signo == 0):
        final = final * -1
    exponent = binario_a_decimal(exponente) - 127
    mantisa2 = '1' + mantisa
    base=mantisa2[0:int(exponent)+1]
    decimal = mantisa2[int(exponent)+1:]
    newBase10=binario_a_decimal(base + "." + decimal)
    return newBase10

def estandarIEEE64Bits_a_decimal(signo,exponente,mantisa):
    print("VALOR")
    final = -1
    if(signo == 0):
        final = final * -1
    exponent = binario_a_decimal(exponente) - 1023
    mantisa2 = '1' + mantisa
    base=mantisa2[0:int(exponent)+1]
    decimal = mantisa2[int(exponent)+1:]
    newBase10=binario_a_decimal(base + "." + decimal)
    return newBase10

#METODOS RAICES
def f(numero, funcion):
    x = numero
    return eval(funcion)

def biseccion(funcion: str, a: float, b: float, errorTolerancia: float):
    iterador = 0
    error_relativo = 0
    raiz_anterior = b
    raiz = 0
    tabla = []
    if f(a, funcion) * f(b, funcion) > 0:
        return "No existen raices en el intervalo"
    else:
        print("FUNCION", f(a, "exp(0.5*x)+cos(x)-4*x**0.5"))
        while iterador <= 50:
            raiz = (a + b) / 2
            if f(raiz, funcion) * f(b, funcion) > 0:
                b = raiz
            else:
                a = raiz 
            error_relativo = abs((raiz_anterior - raiz) / raiz)
            tabla.append([])
            tabla[-1].append(iterador)
            tabla[-1].append(round(float(raiz), 12))
            tabla[-1].append(round(float(f(raiz, funcion)), 12))
            tabla[-1].append(round(float(error_relativo), 12))
            if f(raiz, funcion) == 0 or f(a, funcion) == 0 or f(b, funcion) == 0 or errorTolerancia > error_relativo:
                return tabla
            else:
                iterador+=1
                raiz_anterior = raiz

def regla_falsa(funcion: str, a: float, b: float, errorTolerancia: float):
    iterador = 0
    raiz = 0
    errorRelativo = b
    raizAnterior = 0
    tabla = []
    print("LEYENDO LA FUNCION EN REGLA FALSA ----> ", f(a, funcion))
    if f(a, funcion) * f(b, funcion) < 0:
        while iterador <= 50 and errorRelativo >= errorTolerancia:
            raiz = ((a * f(b, funcion)) - (b * f(a, funcion))) / (f(b, funcion) - f(a, funcion))
            if f(raiz, funcion) * f(b, funcion) < 0:
                a = raiz
            else:
                b = raiz
            errorRelativo = abs((raizAnterior - raiz) / raiz)
            raizAnterior = raiz
            iterador += 1
            tabla.append([])
            tabla[-1].append(iterador)
            tabla[-1].append(round(float(raiz), 12))
            tabla[-1].append(round(float(f(raiz, funcion)), 12))
            tabla[-1].append(round(float(errorRelativo), 12))
    else:
        return "No, no hay raices en el intervalo"
    return tabla

def derivada(funcion, num):
    derivadas = []
    x = Symbol('x')
    try:
        derivadas.append( f(num, str(diff(funcion, x))))
        derivadas.append(diff(funcion, x))
        derivadas.append( f(num, str(diff(funcion, x, 2))))
        derivadas.append(diff(str(derivadas[1]), x))
        return derivadas
    except:
        return None

def newton_raphson(funcion: str, x: float, errorTolerancia: float):
    iterador = 0
    raiz = 0
    raizAnterior = x
    errorRelativo = errorTolerancia
    tabla = []
    while errorRelativo >= errorTolerancia and iterador <= 50:
        raiz = x - (f(x, funcion) / derivada(funcion, x)[0])
        errorRelativo = abs((raizAnterior - raiz) / raiz)
        x = raiz
        raizAnterior = raiz
        iterador += 1
        tabla.append([])
        tabla[-1].append(iterador)
        tabla[-1].append(round(float(raiz), 12))
        tabla[-1].append(round(float(f(raiz, funcion)), 12))
        tabla[-1].append(round(float(errorRelativo), 12))
    return tabla

def secante(funcion:str, a:float, b:float, errorTolerancia:float):
    raiz = float(0)
    raizAnterior = b
    errorRelativo = errorTolerancia
    iterador = int(0)
    tabla = []
    try:
        while errorRelativo >= errorTolerancia and iterador <= 50:
            print("SECANTE")
            print("Resultado", f(10, "log(0.2*x)-sin(0.5*x**(2))+x"))
            raiz = ((a * f(b, funcion)) - (b * f(a, funcion))) / (f(b, funcion) - f(a, funcion))
            errorRelativo = abs((raizAnterior - raiz) / raiz)
            raizAnterior = raiz
            a = b
            b = raiz
            iterador += 1
            tabla.append([])
            tabla[-1].append(iterador)
            tabla[-1].append(round(float(raiz), 12))
            tabla[-1].append(round(float(f(raiz, funcion)), 12))
            tabla[-1].append(round(float(errorRelativo), 12))
        return tabla
    except:
        return None

def grado_polinomio(funcion):
    grado = 0
    for i in range(0, len(funcion)):
        if funcion[i].isnumeric() and funcion[i-3]=='x':
            grado = int(funcion[i])
            break
    return grado

def polinomio(funcion):
    raices = []
    lista = []
    cadena = ""
    dato = funcion
    for i in range(grado_polinomio(funcion), 0, -1):
        dato = dato.replace("x**"+str(i),"r")
    dato = dato.replace("x","r")
    dato = list(map(str, dato))
    for i in range(0,len(dato)):
        if dato[i]=='r' and (dato[i-1]=='+' or dato[i-1]=='-' or i==0):
            dato[i] = "1"
        elif dato[i]=='r' and dato[i-1]=='*':
            dato[i] = ""
    dato = "".join(dato)
    dato = dato.replace('*','')
    dato = dato.replace('+',' ')
    dato = dato.replace('-',' -')
    dato = dato.split(' ')
    for i in range(0,len(dato)-1):
        if dato[i]=='':
            dato.pop(i)
    lista = np.roots(dato)
    for i in range(0, len(lista)):
        cadena = lista[i]
        cadena = str(cadena).replace('j','i')
        cadena = cadena.replace('(','')
        cadena = cadena.replace(')','')
        raices.append(cadena)
    return raices


def es_entero(numero):
    try:
        pos_punto = 0
        for i in range (len(str(numero))):
            if str(numero)[i]=='.':
                pos_punto = i
                break
        if str(numero)[pos_punto+1]!='0' or len(str(numero)[pos_punto:])>2:
            return False
        return True
    except:
        return False

def divisores(numero):
    lista = []
    numero = abs(numero)
    for i in range(1, numero + 1, 1):
        if es_entero(str(numero/i)):
            lista.append(-i)
            lista.append(i)
    return lista

def posibles_raices_gauss(divisores_ti, divisores_cp):
    lista = []
    for i in range(0, len(divisores_ti)):
        for j in range(0, len(divisores_cp)):
            lista.append(divisores_ti[i]/divisores_cp[j])
    return lista

def ruffini(coeficientes, posibles_raices):
    resueltos = []
    multiplicados = []
    raices = []
    raiz_nueva = False
    resueltos.append(coeficientes[0])
    i = 1
    while i < len(posibles_raices):
        for j in range(1, len(coeficientes)):
            multiplicados.append(resueltos[-1] * posibles_raices[i])
            resueltos.append(coeficientes[j]+multiplicados[-1])
            if(resueltos[-1]==0):
                raices.append(posibles_raices[i])
                raiz_nueva = True
        if raiz_nueva:
            coeficientes = resueltos.copy()
            coeficientes.pop()
            raiz_nueva = False
        resueltos.clear()
        multiplicados.clear()
        resueltos.append(coeficientes[0])
        i += 2
    print(raices)

f2="3*x**4+x**3+x**2-6"
f3="x**2+5*x-6"

f4="x**3-x**2-4*x+4"
f5="-x**4+10*x**2-9"
#Raices complejas y reales
f6="4*x**5+8*x**4+9*x**3+9*x**2+5*x+1"

f1="3.5*x**4-8.75*x**3-7.5*x**2+35.25*x-12.45"
f0="-12.105*x**3-67.75*x**2+85.45*x+39.75"
print("HOLA")
#divisores_ti = divisores(12.45)
#divisores_cp = divisores(3.5)
#coeficientes = [3.5,-8.75,-7.5,35.25,12.45]
#posi_raices = posibles_raices_gauss(divisores_ti, divisores_cp)


#print(cambiar_formato_funcion("3*x^2-x^2+sen(2+1)-cos(1)-ln(10)"))

from django.shortcuts import render
from static.lib.Calculadora import *
from static.lib.Utilidad import Utilidad
objCalculadora = Calculadora()
matrices = {}
historial = []
# Create your views here.


def vista_matrices(request):
    titulo = "Matrices"
    paginaPrincipal = "Matrices"
    diccionario = {
        'titulo': titulo,
        'paginaPrincipal': paginaPrincipal,
        'matrices': matrices
    }
    return render(request, 'matrices/matrices.html', context=diccionario)

# Calculo
def guardar_matrices(request):
    nombre = request.POST['nombreMatriz'].upper()
    datos = request.POST['datosMatriz']
    datosTemp = []
    datosMatriz = []
    numCols = 0
    numFils = 1
    fil = 0
    col = 0
    diccionario = {}
    datos = datos.replace("\r\n", ",|,")
    datosTemp = datos.split(",")
    for i in datosTemp:
        if i != '|':
            numCols += 1
        else:
            break
    for i in datosTemp:
        if i == '|':
            numFils += 1
    datosMatriz = np.zeros((numFils, numCols), float)
    for i in datosTemp:
        if i != "|":
            datosMatriz[fil][col] = float(i)
            col += 1
        else:
            fil += 1
            col = 0
    if nombre not in matrices.keys() and nombre.isalpha() == True and nombre != "X" and datos != "":
        matrices[nombre] = datosMatriz
    diccionario = {
        'titulo': "Matrices",
        'paginaPrincipal': "Matrices",
        'matrices': matrices
    }
    return render(request, 'matrices/matrices.html', context=diccionario)


def posicion_matriz(valor, arreglo):
    for i in range(0, len(arreglo)):
        if type(arreglo[i]) == type("") and arreglo[i] == valor:
            return i
    return - 1


def existe_matriz(valor, arreglo):
    for i in range(0, len(arreglo)):
        if type(arreglo[i]) == type("") and arreglo[i] == valor:
            return True
    return False


def solucion_funciones(expresion):
    for i in expresion:
        if type(i) == type(""):
            for j in matrices.keys():
                if f"transpuesta({j})" == i:
                    expresion[posicion_matriz(i, expresion)] = objCalculadora.calcular_matriz(
                        matrices[j], "", "transpuesta", "")
                if f"determinante({j})" == i:
                    expresion[posicion_matriz(i, expresion)] = objCalculadora.calcular_matriz(
                        matrices[j], "", "determinante", "")
                if f"inversa({j})" == i:
                    expresion[posicion_matriz(i, expresion)] = objCalculadora.calcular_matriz(
                        matrices[j], "", "inversa", "")
                if f"rango({j})" == i:
                    expresion[posicion_matriz(i, expresion)] = objCalculadora.calcular_matriz(
                        matrices[j], "", "rango", "")
                if f"triangular({j})" == i:
                    expresion[posicion_matriz(i, expresion)] = objCalculadora.calcular_matriz(
                        matrices[j], "", "triangular", "")
                if f"lu({j})" == i:
                    expresion[posicion_matriz(i, expresion)] = objCalculadora.calcular_matriz(
                        matrices[j], "", "lu", "")
                if f"ajuste({j})" == i:
                    expresion[posicion_matriz(i, expresion)] = objCalculadora.calcular_matriz(matrices[j], "", "ajuste curvas", "")
    return expresion


def reemplazar_nombre_matrices(expresion):
    for i in expresion:
        if type(i) == type("") and len(i) == 1 and i.isalpha():
            if existe_matriz(i, expresion):
                expresion[posicion_matriz(
                    i, expresion)] = matrices[i]
    return expresion


def elevar_matriz(expresion):
    i = 0
    while i < len(expresion):
        if type(expresion[i]) == type(""):
            if expresion[i] == "**":
                posMatriz = i - \
                    1 if type(expresion[i - 1]) != type("") else i + 1
                posNumero = i + 1 if posMatriz == (i - 1) else i - 1
                resultado = objCalculadora.calcular_matriz(
                    expresion[posMatriz], "", "elevar", int(expresion[posNumero]))
                expresion[i - 1] = resultado
                expresion.pop(i)
                expresion.pop(i)
                i = -1
        i += 1
    return expresion


def multiplicar_matriz(expresion):
    i = 0
    while i < len(expresion):
        if type(expresion[i]) == type(""):
            if expresion[i] == "*":
                if type(expresion[i - 1]) != type("") and type(expresion[i + 1]) != type(""):
                    resultado = objCalculadora.calcular_matriz(expresion[i - 1], expresion[i + 1], "multiplicacion", "")
                else:
                    posMatriz = i - 1 if type(expresion[i - 1]) != type("") else i + 1
                    posNumero = i + 1 if posMatriz == (i - 1) else i - 1
                    resultado = objCalculadora.calcular_matriz(expresion[posMatriz], "", "escalar", float(expresion[posNumero]))
                expresion[i - 1] = resultado
                expresion.pop(i)
                expresion.pop(i)
                i = -1
        i += 1
    return expresion

def dividir_matriz(expresion):
    i = 0
    while i < len(expresion):
        if type(expresion[i]) == type(""):
            if expresion[i] == "/":
                if type(expresion[i - 1]) != type("") and type(expresion[i + 1]) != type(""):
                    resultado = objCalculadora.calcular_matriz(expresion[i - 1], expresion[i + 1], "division", "")
                else:
                    posMatriz = i - 1 if type(expresion[i - 1]) != type("") else i + 1
                    posNumero = i + 1 if posMatriz == (i - 1) else i - 1
                    resultado = objCalculadora.calcular_matriz(expresion[posMatriz], float(expresion[posNumero]), "division", "")
                expresion[i - 1] = resultado
                expresion.pop(i)
                expresion.pop(i)
                i = -1
        i += 1
    return expresion

def sumar_restar_matriz(expresion):
    i = 0
    while i < len(expresion):
        if type(expresion[i]) == type(""):
            if expresion[i] in ["+", "-"]:
                if type(expresion[i - 1]) != type("") and type(expresion[i + 1]) != type(""):
                    if expresion[i] == "+":
                        resultado = objCalculadora.calcular_matriz(
                            expresion[i - 1], expresion[i + 1], "suma", "")
                    elif expresion[i] == "-":
                        resultado = objCalculadora.calcular_matriz(
                            expresion[i - 1], expresion[i + 1], "resta", "")
                else:
                    posMatriz = i - 1 if type(expresion[i - 1]) != type("") else i + 1
                    posNumero = i + 1 if posMatriz == (i - 1) else i - 1
                    if expresion[i] == "+":
                        resultado = objCalculadora.calcular_matriz(expresion[posMatriz], float(expresion[posNumero]), "suma", "")
                    elif expresion[i] == "-":
                        resultado = objCalculadora.calcular_matriz(expresion[posMatriz], float(expresion[posNumero]), "resta", "")
                expresion[i - 1] = resultado
                expresion.pop(i)
                expresion.pop(i)
                i = -1
        i += 1
    return expresion


def solucion_operaciones_matriz(expresion):
    existeAjuste = False
    for i in matrices.keys():
        if existe_matriz(f"ajuste({i})", expresion.split(" ")):
            existeAjuste = True
    if existe_matriz("X", expresion) and existe_matriz("=", expresion):
        posMatriz = -1
        posVector = -1
        expresiones = expresion.split("=")
        for i in range(len(expresiones)):
            expresiones[i] = expresiones[i].split(" ")
        expresiones[0].pop(-1)
        expresiones[1].pop(0)
        for i in range(len(expresiones)):
            if existe_matriz("X", expresiones[i]):
                posMatriz = i
            else:
                posVector = i
        expresiones[0] = expresiones[0][:-2]
        print(posMatriz, posVector)
        print(expresiones)
        for i in range(len(expresiones)):
            expresiones[i] = solucion_funciones(expresiones[i])
            expresiones[i] = reemplazar_nombre_matrices(expresiones[i])
            expresiones[i] = elevar_matriz(expresiones[i])
            expresiones[i] = multiplicar_matriz(expresiones[i])
            expresiones[i] = sumar_restar_matriz(expresiones[i])
        expresion = objCalculadora.calcular_matriz(expresiones[posMatriz], expresiones[posVector], "gauss jordan", None)
        print(expresion)
    elif existeAjuste:
        expresion = expresion.split(" ")
        expresion = solucion_funciones(expresion)
    else:
        expresion = expresion.split(" ")
        expresion = solucion_funciones(expresion)
        expresion = reemplazar_nombre_matrices(expresion)
        expresion = elevar_matriz(expresion)
        expresion = multiplicar_matriz(expresion)
        expresion = dividir_matriz(expresion)
        expresion = sumar_restar_matriz(expresion)
    return expresion

def mostrar_calculo_matrices(request):
    diccionario = {}
    expresion = request.POST['entradaExpresionCalculo']
    expresionResultado = ""
    matrizResultado = None
    resultadoUnitario = None
    existeResultado = False
    existeMatrizResultado = False
    historialViual = None
    try:
        print("EXPRESION NORMAL:", expresion)
        expresionResultado = solucion_operaciones_matriz(expresion)
        print(type(expresionResultado[0]) != type(np.array([1,2])))
        if len(expresionResultado) > 1 or type(expresionResultado[0]) == type(None):
            existeResultado = False
        elif type(expresionResultado[0]) != type(np.array([1,2])):
            resultadoUnitario = expresionResultado[0]
            existeMatrizResultado = False
            existeResultado = True
            historial.append({expresion: round(resultadoUnitario, 6)})
        else:
            matrizResultado = expresionResultado[0]
            existeMatrizResultado = True
            existeResultado = True
            historial.append({expresion: matrizResultado})
        if len(historial) > 5:
            historial.pop(0)
        historialViual = historial.copy()
        historialViual.reverse()
        diccionario = {
            'titulo': "Matriz",
            'paginaPrincipal': "Matriz",
            'existeResultado': existeResultado,
            'existeTabla': False,
            'existeGrafico': False,
            'existeTeoria': True,
            'expresionCalculo': expresion,
            'matrizResultado': matrizResultado,
            'resultadoUnitario': resultadoUnitario,
            'existeMatrizResultado': existeMatrizResultado,
            'matrices': matrices,
            'historial': historialViual,
            'expresion': expresion
        }
        return render(request, 'matrices/matrices.html', context=diccionario)
    except:
        return vista_matrices(request)

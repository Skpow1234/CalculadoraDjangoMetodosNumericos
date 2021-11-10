from random import random
from static.lib.Utilidad import *
from static.lib.Derivada import *
from sympy import *
from math import *
import random

class Integral:
    """
    Clase dedicada al calculo de areas bajo la curva

    """

    def integracion_numerica_rectangulos(funcion, a, b, n, metodo):
        """
        Calcular el area bajo la curva de una funcion entre un intervalo [a, b] mediante
        la integracion por rectangulos

        Devuelve el area bajo la curva calculada entre el intervalo especificado

        Parametros
        ---

        funcion: str
            Funcion a integrar
        a: int, float
            Extremo izquierdo el intervalo
        b: int, float
            Extremo derecho del intervalo
        n: int
            Cantidad de divisiones rectangulares en el intervalo
        metodo: str
            Metodo de integracion por rectangulos que se usara para calcular el area bajo la 
        curva, valores aceptados:\n
            "izq" = Integracion numerica por el extremo izquierdo\n
            "der" = Integracion numerica por el extremo derecho\n
            "med" = Integracion numerica por el punto medio\n

        Salidas
        ---

        area: float
            Area bajo la curva calculada

        None:
            Ocurrio un error

        """
        area = 0
        deltaX = (b - a)/n
        valoresX = []
        auxValoresX = []
        valorX = a
        inicioSumatoria = 0
        finalSumatoria = 0
        metodosIntegracionRectangulos = ["izq", "der", "med"]
        msjError = "Error: No se pudo realizar el calculo | Integral.integracion_numerica_rectangulos(funcion, a, b, n, metodo)"
        try:
            for i in range(0, n + 1):
                valoresX.append(valorX)
                valorX += deltaX
            if metodo == metodosIntegracionRectangulos[0]:
                inicioSumatoria = 0
                finalSumatoria = n - 1
            elif metodo == metodosIntegracionRectangulos[1]:
                inicioSumatoria = 1
                finalSumatoria = n
            elif metodo == metodosIntegracionRectangulos[2]:
                inicioSumatoria = 1
                finalSumatoria = n
                for i in range(1, len(valoresX)):
                    valorX = (valoresX[i - 1] + valoresX[i]) / 2
                    auxValoresX.append(valorX)
                valoresX = auxValoresX
            for i in range(inicioSumatoria, finalSumatoria):
                area += Utilidad.evaluar_expresion(valoresX[i], funcion)
            area *= deltaX
            return round(float(area), 12)
        except:
            print(msjError)
            return None


    def integracion_numerica_trapecios(funcion, a, b, n):
        """
        Calcular el area bajo la curva de una funcion entre un intervalo [a, b] mediante
        la integracion por trapecios

        Devuelve el area bajo la curva calculada entre el intervalo especificado

        Parametros
        ---

        funcion: str
            Funcion a integrar
        a: int, float
            Extremo izquierdo el intervalo
        b: int, float
            Extremo derecho del intervalo
        n: int
            Cantidad de divisiones rectangulares en el intervalo

        Salidas
        ---

        area: float
            Area bajo la curva calculada
        error: float
            Error relativo del calculo del area bajo la curva

        None:
            Ocurrio un error

        """
        deltaX = (b - a)/n
        area = 0
        epsilon = a + random.uniform(0, 1) * (b - a)
        error = 0
        lista = []
        msjError = "Error: No se pudo realizar el calculo | Integral.integracion_numerica_trapecios(funcion, a, b, n)"
        try:
            for i in range(0, n + 1):
                lista.append(a+(i*deltaX))
            for i in range(1, n + 1):
                area += (Utilidad.evaluar_expresion(lista[i - 1], funcion) + Utilidad.evaluar_expresion(lista[i], funcion))
            area *= (deltaX/2)
            error = -((deltaX ** 3) / 12) * Derivada.derivada_numerica(funcion, epsilon, 2)
            return round(float(area), 12), round(float(error), 12)
        except:
            print(msjError)
            return None

    def integracion_numerica_simpson1_3(funcion, a, b, n):
        """
        Calcular el area bajo la curva de una funcion entre un intervalo [a, b] mediante
        la integracion por simpson 1/3

        Devuelve el area bajo la curva calculada entre el intervalo especificado

        Parametros
        ---

        funcion: str
            Funcion a integrar
        a: int, float
            Extremo izquierdo el intervalo
        b: int, float
            Extremo derecho del intervalo
        n: int
            Cantidad de divisiones en el intervalo

        Salidas
        ---

        area: float
            Area bajo la curva calculada
        error: float
            Error relativo del calculo del area bajo la curva

        None:
            Ocurrio un error

        """
        lista = []
        deltaX = 0
        area = 0
        epsilon = a + random.uniform(0, 1) * (b - a)
        error = 0
        msjError = "Error: No se pudo realizar el calculo | Integral.integracion_numerica_simpson1_3(funcion, a, b, n)"
        try:
            if n % 2 != 0:
                n += 1
            deltaX = (b-a)/n
            for i in range(0, n + 1):
                lista.append(a+(i*deltaX))
            for i in range(len(lista)):
                if i == 0 or i == len(lista)-1:
                    area += Utilidad.evaluar_expresion(lista[i], funcion)
                elif i % 2 != 0:
                    area += 4 * Utilidad.evaluar_expresion(lista[i], funcion)
                else:
                    area += 2 * Utilidad.evaluar_expresion(lista[i], funcion)
            area *= (deltaX/3)
            error = -((deltaX ** 5)/90) * Derivada.derivada_numerica(funcion, epsilon, 4)
            return round(float(area), 7), round(float(error), 12)
        except:
            print(msjError)
            return None

    def integracion_numerica_simpson3_8(funcion, a, b, n):
        """
        Calcular el area bajo la curva de una funcion entre un intervalo [a, b] mediante
        la integracion por simpson 3/8

        Devuelve el area bajo la curva calculada entre el intervalo especificado

        Parametros
        ---

        funcion: str
            Funcion a integrar
        a: int, float
            Extremo izquierdo el intervalo
        b: int, float
            Extremo derecho del intervalo
        n: int
            Cantidad de divisiones en el intervalo

        Salidas
        ---

        area: float
            Area bajo la curva calculada
        error: float
            Error relativo del calculo del area bajo la curva

        None:
            Ocurrio un error

        """
        area = 0
        deltaX = 0
        valoresX = []
        valorX = a
        error = 0
        epsilon = a + random.uniform(0, 1) * (b - a)
        msjError = "Error: No se pudo realizar el calculo | Integral.integracion_numerica_simpson3_8(funcion, a, b, n)"
        try:
            if Utilidad.evaluar_expresion(a, funcion) >= 0 and Utilidad.evaluar_expresion(b, funcion) >= 0:
                if n % 3 == 1:
                    n += 2
                elif n % 3 == 2:
                    n += 1
                deltaX = (b - a) / n
                for i in range(0, n + 1):
                    valoresX.append(valorX)
                    valorX += deltaX
                for i in range(3, n + 1, 3):
                    area += (3/8) * deltaX * (
                        Utilidad.evaluar_expresion(valoresX[i - 3], funcion) +
                        3 * Utilidad.evaluar_expresion(valoresX[i - 2], funcion) +
                        3 * Utilidad.evaluar_expresion(valoresX[i - 1], funcion) +
                        Utilidad.evaluar_expresion(valoresX[i], funcion)
                    )
                error = -(3/80) * (deltaX ** 5) * Derivada.derivada_numerica(funcion, epsilon, 4)
                return round(float(area), 7), round(float(error), 12)
        except:
            print(msjError)
            return None

    def integracion_numerica_montecarlo(funcion, a, b, n):
        """
        Calcular el area bajo la curva de una funcion entre un intervalo [a, b] mediante
        la integracion por montecarlo

        Devuelve el area bajo la curva calculada entre el intervalo especificado

        Parametros
        ---

        funcion: str
            Funcion a integrar
        a: int, float
            Extremo izquierdo el intervalo
        b: int, float
            Extremo derecho del intervalo
        n: int
            Cantidad de puntos generados aleatoriamente

        Salidas
        ---

        area: float
            Area bajo la curva calculada
        nExitos: int
            Numero de puntos dentro del area

        None:
            Ocurrio un error

        """
        area = 0
        nExitos = 0
        x = 0
        y = 0
        m = 0
        i = a
        p = []
        msjError = "Error: No se pudo realizar el calculo | Integral.integracion_numerica_montecarlo(funcion, a, b, n)"
        try:
            while i <= b:
                p.append(i)
                i += 0.1
            for i in p:
                if Utilidad.evaluar_expresion(i, funcion) >= m:
                    m = Utilidad.evaluar_expresion(i, funcion)
            for i in range(0, n + 1):
                x = (b - a) * random.uniform(0, 1) + a
                y = m * random.uniform(0, 1)
                if y <= Utilidad.evaluar_expresion(x, funcion):
                    nExitos += 1
            area = (nExitos/n) * (b - a) * m
            return area, nExitos
        except:
            print(msjError)
            return None


funcion = "x**5+1"
a = 2
b = 10
n = 10000
Integral.integracion_numerica_montecarlo("x**2", a, b, n)
#print("IZQ:", Integral.integracion_numerica_rectangulos(funcion, a, b, n, "izq"))
#print("DER:", Integral.integracion_numerica_rectangulos(funcion, a, b, n, "der"))
#print("MED:", Integral.integracion_numerica_rectangulos(funcion, a, b, n, "med"))
#print("TRP:", Integral.integracion_numerica_trapecios(funcion, a, b, n))
#print("S13:", Integral.integracion_numerica_simpson1_3(funcion, a, b, n))
#print("S38:", Integral.integracion_numerica_simpson3_8(funcion, a, b, n))
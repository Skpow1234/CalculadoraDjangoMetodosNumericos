from static.lib.Derivada import *
from static.lib.Utilidad import *
from sympy import *
from math import *
from numpy import *
from decimal import Decimal, getcontext

class Raiz:

    def __init__(self, cantidadIteraciones=100, cantidadDecimales=7):
        """
        Clase dedicada a la busqueda de raices en una funcion matematica

        Parametros
        ---

        cantidadIteraciones: int, opcional
            Cantidad limite de iteraciones que realizan los metodos para encontrar la raiz
        cantidadDecimales: int, opcional
            Cantidad de decimales que se mostraran en los resultados

        """
        self.iteraciones = 50 if cantidadIteraciones <= 0 else cantidadIteraciones
        self.cantidadDecimales = 7 if cantidadDecimales <=0 else cantidadDecimales

    def biseccion(self, expresion, a, b, errorTolerancia):
        """
        Encontrar la raiz de una funcion entre dos intervalos por el metodo de Biseccion

        Devuelve una lista de listas conformadas por el numero de iteracion, raiz, limite inferior, limite superior, error relativo

        Parametros
        ---
        
        expresion: str
            Expresion de una funcion matematica
        a: float
            Limite inferior del intervalo
        b: float
            Limite superior del intervalo
        errorTolerancia: float
            Precision esperada de al encontrar la raiz
        
        Salidas
        ---
        
        tabla: list
            Lista de listas en formato iteracion, raiz, limite inferior, limite superior, error relativo
        msjNoRaices: str
            Mensaje al no haber raices en el intervalo

        None:
            Ocurrio un error

        """
        iterador = 0
        errorRelativo = 0.0
        raiz_anterior = b
        raiz = 0.0
        tabla = []
        msjError = "Error: No se pudo realizar el calculo | Raiz.biseccion(expresion, a, b, errorTolerancia)"
        msjNoRaices = "No hay raices en el intervalo"
        try:
            if Utilidad.evaluar_expresion(a, expresion) * Utilidad.evaluar_expresion(b, expresion) > 0:
                return msjNoRaices
            else:
                while iterador <= self.iteraciones:
                    raiz = (a + b) / 2
                    if Utilidad.evaluar_expresion(raiz, expresion) * Utilidad.evaluar_expresion(b, expresion) > 0:
                        b = raiz
                    else:
                        a = raiz 
                    errorRelativo = abs((raiz_anterior - raiz) / raiz)
                    if  Utilidad.evaluar_expresion(raiz, expresion) == 0 or Utilidad.evaluar_expresion(a, expresion) == 0 or Utilidad.evaluar_expresion(b, expresion) == 0 or errorTolerancia > errorRelativo:
                        tabla.append([
                            iterador,
                            round(float(a), self.cantidadDecimales),
                            round(float(b), self.cantidadDecimales),
                            round(float(Utilidad.evaluar_expresion(a, expresion)), 12),
                            round(float(Utilidad.evaluar_expresion(b, expresion)), 12),
                            round(raiz, self.cantidadDecimales), 
                            round(float(Utilidad.evaluar_expresion(raiz, expresion)), 12),
                            round(float(errorRelativo), 12)])
                        return tabla
                    else:
                        iterador+=1
                        raiz_anterior = raiz
                        tabla.append([
                            iterador,
                            round(float(a), self.cantidadDecimales),
                            round(float(b), self.cantidadDecimales),
                            round(float(Utilidad.evaluar_expresion(a, expresion)), 12),
                            round(float(Utilidad.evaluar_expresion(b, expresion)), 12),
                            round(raiz, self.cantidadDecimales), 
                            round(float(Utilidad.evaluar_expresion(raiz, expresion)), 12),
                            round(float(errorRelativo), 12)])
        except:
            print(msjError)
            return None
 

    def regla_falsa(self, expresion, a, b, errorTolerancia):
        """
        Encontrar la raiz de una funcion entre dos intervalos por el metodo de Regla falsa

        Devuelve una lista de listas conformadas por el numero de iteracion, raiz, limite inferior, limite superior, error relativo

        Parametros
        ---
        
        expresion: str
            Expresion de una funcion matematica
        a: float
            Limite inferior del intervalo
        b: float
            Limite superior del intervalo
        errorTolerancia: float
            Precision esperada de al encontrar la raiz
        
        Salidas
        ---
        
        tabla: list
            Lista de listas en formato iteracion, raiz, limite inferior, limite superior, error relativo
        msjNoRaices: str
            Mensaje al no haber raices en el intervalo

        None:
            Ocurrio un error

        """
        iterador = 0
        raiz = 0
        errorRelativo = b
        raizAnterior = 0
        tabla = []
        msjError = "Error: No se pudo realizar el calculo | Raiz.regla_falsa(expresion, a, b, errorTolerancia)"
        msjNoRaices = "No hay raices en el intervalo"
        try:
            if Utilidad.evaluar_expresion(a, expresion) * Utilidad.evaluar_expresion(b, expresion) < 0:
                while iterador <= self.iteraciones and errorRelativo >= errorTolerancia:
                    iterador += 1
                    raiz = ((a * Utilidad.evaluar_expresion(b, expresion)) - (b * Utilidad.evaluar_expresion(a, expresion))) / (Utilidad.evaluar_expresion(b, expresion) - Utilidad.evaluar_expresion(a, expresion))
                    tabla.append([
                            iterador,
                            round(float(a), self.cantidadDecimales),
                            round(float(b), self.cantidadDecimales),
                            round(float(Utilidad.evaluar_expresion(a, expresion)), 12),
                            round(float(Utilidad.evaluar_expresion(b, expresion)), 12),
                            round(raiz, self.cantidadDecimales), 
                            round(float(Utilidad.evaluar_expresion(raiz, expresion)), 12),
                            round(float(errorRelativo), 12)])
                    if Utilidad.evaluar_expresion(raiz, expresion) * Utilidad.evaluar_expresion(b, expresion) < 0:
                        a = raiz
                    else:
                        b = raiz
                    errorRelativo = abs((raizAnterior - raiz) / raiz)
                    raizAnterior = raiz
            else:
                return msjNoRaices
            return tabla
        except:
            print(msjError)
            return None

    def newton_raphson(self, expresion, x, errorTolerancia):
        """
        Encontrar la raiz de una funcion usando el metodo de Newton Raphson

        Devuelve una lista de listas conformadas por el numero de iteracion, raiz, limite inferior, limite superior, error relativo

        Parametros
        ---
        
        expresion: str
            Expresion de una funcion matematica
        x: float
            Valor numerico inicial
        errorTolerancia: float
            Precision esperada al encontrar la raiz
        
        Salidas
        ---
        
        tabla: list
            Lista de listas en formato iteracion, raiz, limite inferior, limite superior, error relativo
        
        None:
            Ocurrio un error

        """
        iterador = 0
        raiz = 0.0
        raizAnterior = x
        errorRelativo = errorTolerancia
        tabla = []
        msjError = "Error: No se pudo realizar el calculo | Raiz.newton_raphson(expresion, x, errorTolerancia)"
        try:
            while errorRelativo >= errorTolerancia and iterador <= self.iteraciones:
                iterador += 1
                raiz = x - (Utilidad.evaluar_expresion(x, expresion) / Derivada.derivada_numerica(expresion, x, 1))
                errorRelativo = abs((raizAnterior - raiz) / raiz)
                raizAnterior = raiz
                tabla.append([
                    iterador,
                    round(x, self.cantidadDecimales),
                    round(raiz, self.cantidadDecimales), 
                    round(float(Utilidad.evaluar_expresion(raiz, expresion)), 12), 
                    round(float(errorRelativo), 12)])
                x = raiz
            return tabla
        except:
            print(msjError)
            return None
        

    def secante(self, expresion, a, b, errorTolerancia):
        """
        Encontrar la raiz de una funcion entre dos intervalos por el metodo de la Secante

        Devuelve una lista de listas conformadas por el numero de iteracion, raiz, limite inferior, limite superior, error relativo

        Parametros
        ---
        
        expresion: str
            Expresion de una funcion matematica
        a: float
            Limite inferior del intervalo
        b: float
            Limite superior del intervalo
        errorTolerancia: float
            Precision esperada de al encontrar la raiz
        
        Salidas
        ---
        
        tabla: list
            Lista de listas en formato iteracion, raiz, limite inferior, limite superior, error relativo
        
        None:
            Ocurrio un error

        """
        raiz = 0.0
        raizAnterior = b
        errorRelativo = errorTolerancia
        iterador = 0
        tabla = []
        msjError = "Error: No se pudo realizar el calculo | Raiz.secante(expresion, a, b, errorTolerancia)"
        try:
            while errorRelativo >= errorTolerancia and iterador <= self.iteraciones:
                iterador += 1
                raiz = ((a * Utilidad.evaluar_expresion(b, expresion)) - (b * Utilidad.evaluar_expresion(a, expresion))) / (Utilidad.evaluar_expresion(b, expresion) - Utilidad.evaluar_expresion(a, expresion))
                errorRelativo = abs((raizAnterior - raiz) / raiz)
                raizAnterior = raiz
                tabla.append([
                    iterador,
                    round(float(a), self.cantidadDecimales),
                    round(float(b), self.cantidadDecimales),
                    round(float(Utilidad.evaluar_expresion(a, expresion)), 12),
                    round(float(Utilidad.evaluar_expresion(b, expresion)), 12),
                    round(raiz, self.cantidadDecimales), 
                    round(float(Utilidad.evaluar_expresion(raiz, expresion)), 12),
                    round(float(errorRelativo), 12)])
                a = b
                b = raiz
            return tabla
        except:
            print(msjError)
            return None

    def polinomio(self, expresion):
        """
        Encontrar las raices de funciones polinomicas

        Devuelve una lista con las raices calculadas para la funcion

        Parametros
        ---
        
        expresion: str
            Expresion de una funcion polinomica
        
        Salidas
        ---
        
        raices: list
            Lista con las raices calculadas
        
        None:
            Ocurrio un error

        """
        raices = []
        lista = []
        cadena = ""
        dato = expresion
        msjError = "Error: No se pudo realizar el calculo | Raiz.polinomio(expresion)"
        try:
            for i in range(self._grado_polinomio(expresion), 0, -1):
                dato = dato.replace("(x**"+str(i)+")","r")
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
            print("FUNCION:", dato)
            lista = roots(dato)
            for i in range(0, len(lista)):
                cadena = lista[i]
                cadena = str(cadena).replace('j','i')
                cadena = cadena.replace('(','')
                cadena = cadena.replace(')','')
                raices.append(cadena)
            return raices
        except:
            print(msjError)
            return None

    def _grado_polinomio(self, expresion):
        """
        Calcular el grado de un polinomio

        Devuelve el grado del polinomio

        Parametros
        ---
        
        expresion: str
            Expresion de una funcion polinomica
        
        Salidas
        ---
        
        grado: int
            Grado del polinomio
        
        None:
            Ocurrio un error

        """
        grado = 0
        msjError = "Error: No se pudo realizar el calculo | Raiz._grado_polinomio(expresion)"
        try:
            for i in range(0, len(expresion)):
                if expresion[i].isnumeric() and expresion[i-3]=='x':
                    grado = int(expresion[i])
                    break
            return grado
        except:
            print(msjError)
            return None
from sympy.strategies.core import switch
from static.lib.Utilidad import Utilidad
from static.lib.Conversion import Conversion
from static.lib.Raiz import Raiz
from static.lib.Derivada import Derivada
from static.lib.Integral import Integral
from static.lib import Matriz
from math import *
import numpy as np
import matplotlib.pyplot as plt
import os

class Calculadora:
    objConversion = Conversion()
    objRaiz = Raiz()

    def convertir_bases(self, valor, baseActual, baseNueva):
        """
        Convierte entre sistemas numericos

        Devuelve un valor en la base numerica especificada

        Parametros
        ---

        valor: str
            Valor a calcular en la nueva base
        baseActual: int
            Base numerica en la que esta el valor
        baseNueva: int
            Base numerica en la que se calculara el valor

        Salidas
        ---

        resultado: str
            Resultado del valor calculado en la nueva base numerica

        """
        resultado = ""
        if baseActual == 2:
            if baseNueva == 8:
                resultado = self.objConversion.binario_a_octal(valor)
            elif baseNueva == 10:
                resultado = self.objConversion.binario_a_decimal(valor)
            elif baseNueva == 16:
                resultado = self.objConversion.binario_a_hexadecimal(valor)
        elif baseActual == 8:
            if baseNueva == 2:
                resultado = self.objConversion.octal_a_binario(valor)
            elif baseNueva == 10:
                resultado = self.objConversion.octal_a(valor, baseNueva)
            elif baseNueva == 16:
                resultado = self.objConversion.octal_a_hexadecimal(valor)
        elif baseActual == 10:
            if baseNueva == 75432:
                resultado = self.objConversion.base10_a_IEEE32bits(valor)
            elif baseNueva == 75464:
                resultado = self.objConversion.base10_a_IEEE64bits(valor)
            else:
                resultado = self.objConversion.decimal_a(valor, baseNueva)    
        elif baseActual == 16:
            if baseNueva == 2:
                resultado = self.objConversion.hexadecimal_a_binario(valor)
            elif baseNueva == 8:
                resultado = self.objConversion.hexadecimal_a_octal(valor)
            elif baseNueva == 10:
                resultado = self.objConversion.hexadecimal_a_decimal(valor)
        return resultado

    def ieee754_a_decimal(self, signo, exponente, mantisa, bits):
        if bits == 32:
            resultado = self.objConversion.IEEE32Bits_a_decimal(signo, exponente, mantisa)
        elif bits == 64:
            resultado = self.objConversion.IEEE64Bits_a_decimal(signo, exponente, mantisa)
        return resultado

    def calcular_raices(self, nombreMetodo, expresion, limiteInferior, limiteSuperior, errorTolerancia):
        expresion = Utilidad.formatear_expresion(expresion)
        raices = []
        if nombreMetodo == "biseccion":
            raices = self.objRaiz.biseccion(expresion, limiteInferior, limiteSuperior, errorTolerancia)
        elif nombreMetodo == "regla falsa":
            raices = self.objRaiz.regla_falsa(expresion, limiteInferior, limiteSuperior, errorTolerancia)
        elif nombreMetodo == "newton raphson":
            raices = self.objRaiz.newton_raphson(expresion, limiteInferior, errorTolerancia)
        elif nombreMetodo == "secante":
            raices = self.objRaiz.secante(expresion, limiteInferior, limiteSuperior, errorTolerancia)
        elif nombreMetodo == "polinomio":
            raices = self.objRaiz.polinomio(expresion)
        return raices
    
    def calcular_derivada_numerica(self, expresion, numero, orden):
        expresion = Utilidad.formatear_expresion(expresion)
        derivada = Derivada.derivada_numerica(expresion, numero, orden)
        return derivada
    
    def calcular_derivada_simbolica(self, expresion, orden):
        expresion = Utilidad.formatear_expresion(expresion)
        derivada = Derivada.derivada_simbolica(expresion, orden)
        return derivada

    def calcular_integral_numerica(self, metodo, expresion, extremoIzquierdo, extremoDerecho, cantidadDivisiones):
        expresion = Utilidad.formatear_expresion(expresion)
        metodosIntegracionRectangulos = ["izq", "der", "med"]
        resultado = 0
        if metodo in metodosIntegracionRectangulos:
            resultado = Integral.integracion_numerica_rectangulos(expresion, extremoIzquierdo, extremoDerecho, cantidadDivisiones, metodo)
        elif metodo == "trapecios":
            resultado = Integral.integracion_numerica_trapecios(expresion, extremoIzquierdo, extremoDerecho, cantidadDivisiones)
        elif metodo == "simpson 1/3":
            resultado = Integral.integracion_numerica_simpson1_3(expresion, extremoIzquierdo, extremoDerecho, cantidadDivisiones)
        elif metodo == "simpson 3/8":
            resultado = Integral.integracion_numerica_simpson3_8(expresion, extremoIzquierdo, extremoDerecho, cantidadDivisiones)
        elif metodo == "montecarlo":
            resultado = Integral.integracion_numerica_montecarlo(expresion, extremoIzquierdo, extremoDerecho, cantidadDivisiones)
        return resultado

    def calcular_matriz(self, matrizA, matrizB, operacion, numero):
        resultado = []
        if operacion == "transpuesta":
            resultado = Matriz.transpuesta(matrizA)
        elif operacion == "determinante":
            resultado = Matriz.determinante(matrizA)
        elif operacion == "inversa":
            resultado = Matriz.inversa(matrizA)
        elif operacion == "rango":
            resultado = Matriz.rango(matrizA)
        elif operacion == "triangular":
            resultado = Matriz.triangular(matrizA)
        elif operacion == "lu":
            resultado = Matriz.factorizacionLU(matrizA)
        elif operacion == "ajuste curvas":
            resultado = Matriz.ajuste_curvas(matrizA)
        elif operacion == "suma":
            resultado = Matriz.suma(matrizA, matrizB)
        elif operacion == "resta":
            resultado = Matriz.resta(matrizA, matrizB)
        elif operacion == "multiplicacion":
            resultado = Matriz.multiplicacion(matrizA, matrizB)
        elif operacion == "division":
            resultado = Matriz.division(matrizA, matrizB)
        elif operacion == "gauss jordan":
            resultado = Matriz.gauss_jordan(matrizA, matrizB)
        elif operacion == "escalar":
            resultado = Matriz.escalar(matrizA, numero)
        elif operacion == "elevar":
            resultado = Matriz.elevacion(matrizA, numero)
        return resultado

    def generar_grafico(funcion, xInicial=-10, xFinal=10, xTam=8, yTam=5):
        """
        Genera el grafico de una funcion matematica en un intervalo de valores

        Parametros
        ---

        funcion: str 
            funcion matematica
        xInicial: int, float, opcional
            Valor inicial del eje x
        yFinal: int, float, opcional
            Valor final del eje x
        xTam: int, float, opcional
            Tamaño del grafico en x
        yTam: int, float, opcional
            Tamaño del grafico en y
        
        Salidas
        ---
        
        None:
            Ocurrio un error

        """      
        x = []
        y = []
        ruta = "static/img/grafico.png"
        funcion = Utilidad.formatear_expresion(funcion)
        msjError = "Error: No se pudo generar el grafico | Calculadora.graficar_funcion(funcion)"
        try:
            if os.path.exists(ruta):
                os.remove(ruta)
            if "log" in funcion:
                x = np.linspace(0.1e-1, xFinal * 2, num=1000)
            else:
                x = np.linspace(xInicial, xFinal, num=1000)
            for i in x:
                y.append(Utilidad.evaluar_expresion(i, funcion))
            plt.figure(figsize=(xTam, yTam))
            plt.title("f(x) = " + Utilidad.regular_expresion(funcion))
            plt.grid()
            plt.plot(x, y)
            ax = plt.gca()
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.spines['bottom'].set_position(('data',0))
            ax.yaxis.set_ticks_position('left')
            ax.spines['left'].set_position(('data',0))
            plt.savefig(ruta)
        except:
            print(msjError)
            return None



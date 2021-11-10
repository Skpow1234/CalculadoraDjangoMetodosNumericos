from static.lib.Utilidad import *
from sympy import *
from math import *

class Derivada:
    """
    Clase dedicada al calculo numerico y simbolico de derivadas
    
    """

    def derivada_numerica(expresion, numero, orden):
        """
        Calcular la derivada numerica de una expresion matematica

        Devuelve el valor numerico calculado al evaluar la derivada con el numero especificado
        
        Parametros
        ---

        expresion: str
            Expresion matematica
        numero: float, int
            Numero a evaluar
        orden: int
            Orden de la derivada

        Salidas
        ---

        derivadaNumerica: float
            Valor numerico calculado

        None:
            Ocurrio un error

        """
        derivadaNumerica = 0.0
        msjError = "Error: No se pudo realizar el calculo | Derivada.derivada_numerica(expresion, numero)"
        try:
            derivadaNumerica = Utilidad.evaluar_expresion(numero, Derivada.derivada_simbolica(expresion, orden))
            return round(float(derivadaNumerica), 7)
        except:
            print(msjError)
            return None

    def derivada_simbolica(expresion, orden):
        """
        Calcular la derivada simbolica de una expresion matematica

        Devuelve la derivada simbolica calculada al evaluar la derivada en el orden especificado

        Parametros
        ---

        expresion: str
            Expresion matematica
        orden: int
            Orden de la derivada

        Salidas
        ---

        derivadaSimbolica: str
            Expresion resultante al derivar
            
        None:
            Ocurrio un error

        """
        funcion = expresion
        derivadaSimbolica = ""
        msjError = "Error: No se pudo realizar el calculo | Derivada.derivada_simbolica(expresion)"
        x = Symbol('x')
        try:
            for i in range(0, orden):
                derivadaSimbolica = diff(funcion, x)
                funcion = derivadaSimbolica
            return str(derivadaSimbolica)
        except:
            print(msjError)
            return None
from math import *

class Utilidad:
    """
    Clase dedicada a diversos metodos utiles

    """
    
    def quitar_espacios(cadena):
        """
        Quita los espacios en una cadena

        Parametros
        ---
        
        cadena: str
            Cadena de texto

        Salidas
        ---

        cadenaSinEspacios: str
            Cadena de texto proporcionanda sin espacios

        None:
            Ocurrio un error

        """
        cadenaSinEspacios = ""
        msjError = "Error: No se pudo quitar los espacios | Utilidad.quitar_espacios(cadena)"
        try:
            cadenaSinEspacios = cadena
            cadenaSinEspacios = cadenaSinEspacios.replace(' ', '')
            return str(cadenaSinEspacios)
        except:
            print(msjError)
            return None

    def formatear_expresion(expresion):
        """
        Formatear una expresion matematica a formato Python
        
        Devuelve un str el cual es la expresion en formato Python haciendo
        uso del metodo replace

        Parametros
        ---
        
        expresion: str
            Expresion matematica

        Salidas
        ---

        exprFormateada: str
            Expresion en formato Python

        None:
            Ocurrio un error

        """
        exprFormateada = ""
        msjError = "Error: No se pudo fromatear la expresion | Utilidad.formatear_expresion(expresion)"
        try:
            exprFormateada = expresion
            exprFormateada = exprFormateada.replace('ln', 'log')
            exprFormateada = exprFormateada.replace('sen', 'sin')
            exprFormateada = exprFormateada.replace('^', '**')
            return str(exprFormateada)
        except:
            print(msjError)
            return None

    def regular_expresion(expresion):
        """
        Formatear una expresion en formato Python a una matematica
        
        Devuelve un str el cual es la expresion en formato matematico haciendo
        uso del metodo replace

        Parametros
        ---

        expresionFormateada: str 
            Expresion en formato Python
        
        Salidas
        ---

        exprRegular: str
            Expresion en formato general

        None:
            Ocurrio un error

        """
        exprRegular = ""
        msjError = "Error: No se pudo regular la expresion | Utilidad.regular_expresion(expresion)"
        try:
            exprRegular = expresion
            exprRegular = exprRegular.replace('log', 'ln')
            exprRegular = exprRegular.replace('sin', 'sen')
            exprRegular = exprRegular.replace('**', '^')
            return str(exprRegular)
        except:
            print(msjError)
            return None

    def evaluar_expresion(numero, expresion):
        """
        Calcular el resultado de un numero en una expresion matematica

        Devuelve un str el cual es el resultado del calculo del numero en la expresion
        matematica haciendo uso del metodo eval

        Parametros
        ---

        numero: float 
            Valor numerico a calcular
        
        Salidas
        ---
        
        resultado: float
            Valor numerico resultante de realizar el calculo de numero en la expresion

        None:
            Ocurrio un error

        """
        x = numero
        expr = expresion
        msjError = "Error: No se pudo realizar el calculo | Utilidad.evaluar_expresion(numero, expresion)"
        try:
            resultado = round(eval(expr), 12)
            return float(resultado)
        except:
            print(msjError)
            return None

    def redondear_matriz(matriz):
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                matriz[i][j] = round(matriz[i][j], 12)
        return matriz


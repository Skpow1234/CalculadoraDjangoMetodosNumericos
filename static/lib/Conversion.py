class Conversion:

    def __init__(self, cantidadDecimales=12):
        """
        Clase dedicada a la conversion entre sistemas numericos

        Parametros
        ---
        
        cantidadDecimales: int, opcional
            Cantidad de decimales que se muestran en los resultados

        """
        self.limiteDecimales = cantidadDecimales if cantidadDecimales>0 else 12

    def decimal_a(self, valor, base):
        numero = 0
        resultado = 0
        baseActual = 10
        baseNueva = 0
        parteEntera = 0
        parteDecimal = 0
        try:
            baseNueva = int(base)
            numero = str(float(valor)).split('.')
            parteEntera = self._parte_entera_base10(int(numero[0]), baseActual, baseNueva)
            resultado = parteEntera
            if len(numero) > 1 and numero[1] != "0":
                parteDecimal = self._parte_decimal_base10(float("0." + numero[1]), baseActual, baseNueva)
                resultado = resultado + "." + parteDecimal
            return resultado
        except:
            return None

    def _parte_entera_base10(self, valor, baseActual, baseNueva):
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
                resultado = str(resultado)[:len(str(resultado))]
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

    def _parte_decimal_base10(self, valor, baseActual, baseNueva):
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
            while iterador < self.limiteDecimales:
                numero = numero * baseNueva
                lista.append(int(numero))
                numero = numero - lista[-1]
                iterador = iterador + 1
            iterador = 1
            if baseNueva != 16:
                while iterador <= self.limiteDecimales:
                    resultado = resultado + lista[iterador - 1] * pow(baseActual, iterador * -1)
                    iterador = iterador + 1
                resultado = str(round(resultado, self.limiteDecimales))[2:]
            else:
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
    def binario_a_decimal(self, valor):
        numero = []
        potencia = 0
        resultado =  0
        parteEntera = 0
        parteDecimal = 0
        iterador = 0
        try:
            numero = str(valor).split('.')
            parteEntera = list(map(int, numero[0]))
            potencia = len(parteEntera) - 1
            for i in parteEntera:
                resultado = resultado + (i * pow(2, potencia))
                potencia = potencia - 1
            if len(numero) > 1:
                parteDecimal = list(map(int, numero[1]))
                while iterador < self.limiteDecimales:
                    if iterador < len(parteDecimal):
                        resultado = resultado + (parteDecimal[iterador] * pow(2, potencia))
                        potencia = potencia - 1
                    iterador = iterador + 1
            return resultado
        except:
            return None

    def binario_a_hexadecimal(self, valor):
        numero = ""
        parteEntera = ""
        parteDecimal = ""
        resultado = ""
        try:
            numero = str(valor).split('.')
            parteEntera = self._a_hexadecimal(numero[0])
            resultado = parteEntera
            if len(numero) > 1:
                parteDecimal = self._a_hexadecimal(numero[1])
                resultado = resultado + "." + parteDecimal
            return resultado
        except:
            return None

    def binario_a_octal(self, valor):
        numero = 0
        parteEntera = 0
        parteDecimal = 0
        resultado = 0
        try:
            numero = str(valor).split('.')
            parteEntera = self._a_octal(numero[0])
            resultado = parteEntera
            if len(numero) > 1:
                parteDecimal = self._a_octal(numero[1])
                resultado = resultado + "." + parteDecimal
            return resultado
        except:
            return None

    def _a_hexadecimal(self, valor):
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

    def _a_octal(self, valor: str):
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
    def octal_a(self, valor, base):
        numero = 0
        resultado = 0
        baseActual = 8
        baseNueva = 0
        parteEntera = 0
        parteDecimal = 0
        try:
            baseNueva = int(base)
            numero = float(valor)
            parteEntera, parteDecimal = str(numero).split('.')
            resultado = self._parte_entera_base8(int(parteEntera), baseActual, baseNueva)
            if int(parteDecimal) > 0:
                resultado = resultado + "." + self._parte_decimal_base8(float("0." + parteDecimal), baseActual, baseNueva)
            return resultado
        except:
            return None

    def _parte_entera_base8(self, valor, baseActual, baseNueva):
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

    def _parte_decimal_base8(self, valor, baseActual, baseNueva):
        iterador = 0
        lista = []
        resultado = 0
        numero = valor
        iterador = 0
        try:
            while iterador < self.limiteDecimales:
                numero = numero * baseNueva
                lista.append(int(numero))
                numero = numero - lista[-1]
                iterador = iterador + 1
            iterador = 1
            while iterador < self.limiteDecimales:
                resultado = resultado + lista[iterador - 1] * pow(baseActual, iterador * -1)
                iterador = iterador + 1
            resultado = str(round(resultado, self.limiteDecimales + 1))[2:]
            return resultado 
        except:
            return None

    def octal_a_binario(self, valor):
        numero = 0
        resultado = 0
        parteEntera = 0
        parteDecimal = 0
        try:
            numero = float(valor)
            numero = str(numero).split('.')
            parteEntera = self._a_binario(int(numero[0]))
            resultado = parteEntera
            if len(numero) > 0:
                parteDecimal = self._a_binario(int(numero[1]))
            resultado = resultado + "." + parteDecimal
            return resultado
        except:
            return None

    def _a_binario(self, valor):
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

    def octal_a_hexadecimal(self, valor):
        numero = 0
        resultado = 0
        parteEntera = 0
        parteDecimal = 0
        try:
            numero = str(float(valor)).split('.')
            parteEntera = self.binario_a_hexadecimal(self.a_binario(int(numero[0])))
            resultado = parteEntera
            if len(numero) > 1:
                parteDecimal = self.binario_a_hexadecimal(self.a_binario(int(numero[1])))
            resultado = resultado + "." + parteDecimal
            return resultado
        except:
            return None 

    #HEXADECIMAL
    def hexadecimal_a_decimal(self, valor):
        numero = 0
        parteEntera = []
        parteDecimal = 0
        try:
            numero = str(valor).split('.')
            parteEntera = list(numero[0].upper())
            resultado = self._parte_entera_base16(parteEntera)
            if len(numero) > 1 and numero[1] != "0":
                parteDecimal = self._parte_decimal_base16(list(numero[1].upper()))
                resultado = resultado + "." + parteDecimal
            return resultado
        except:
            return None

    def _parte_entera_base16(self, parteEntera):
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

    def _parte_decimal_base16(self, parteDecimal):
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

    def hexadecimal_a_octal(self, valor):
        return self.decimal_a(self.hexadecimal_a_decimal(valor), 8)

    def hexadecimal_a_binario(self, valor):
        return self.decimal_a(self.hexadecimal_a_decimal(valor), 2)

    #ESTANDAR IEEE
    def base10_a_IEEE32bits(self, numero):
        auxNumero = list(numero)
        noCerosIzq = False
        signo = self._signoestandarIEEE(numero)
        exponente = ""
        mantisa = ""
        if signo == '1':
            numero = "".join(list(numero)[1:])
        numero = self.decimal_a(numero, 2)
        while noCerosIzq != True:
            if auxNumero[0] == '0':
                auxNumero.pop(0)
            else:
                noCerosIzq = True
        exponente = self._exponenteestandarIEEE32bits(numero)
        mantisa = self._mantisaestandarIEEE32bits(numero)
        return signo, exponente, mantisa

    def _signoestandarIEEE(self, numero):
        signo = ''
        msjError = "Error: No se pudo realizar el calculo | Conversion._signoestandarIEEE(numero)"
        try:
            if numero[0] == '-':
                signo = '1'
            else:
                signo = '0'
            return signo
        except:
            print(msjError)
            return None

    def _exponenteestandarIEEE32bits(self, numero):
        posPunto = 0
        exponente = 0
        msjError = "Error: No se pudo realizar el calculo | Conversion._exponenteestandarIEEE32bits(numero)"
        try:
            for i in range(0, len(numero)):
                if numero[i] != '.':
                    posPunto += 1
                else:
                    posPunto -= 1
                    break
            exponente = posPunto + 127
            exponente = self.decimal_a(exponente, 2)
            return exponente
        except:
            print(msjError)
            return None

    def _mantisaestandarIEEE32bits(self, numero):
        mantisa = ""
        msjError = "Error: No se pudo realizar el calculo | Conversion._mantisaestandarIEEE32bits(numero)"
        try:
            mantisa = numero.replace('.', '')
            mantisa = list(mantisa)
            while len(mantisa[1:]) < 23:
                mantisa.append('0')
            mantisa = "".join(list(mantisa)[1:24])
            return mantisa
        except:
            print(msjError)
            return None

    def base10_a_IEEE64bits(self, numero):
        auxNumero = list(numero)
        noCerosIzq = False
        signo = self._signoestandarIEEE(numero)
        exponente = ""
        mantisa = ""
        if signo == '1':
            numero = "".join(list(numero)[1:])
        numero = self.decimal_a(numero, 2)
        while noCerosIzq != True:
            if auxNumero[0] == '0':
                auxNumero.pop(0)
            else:
                noCerosIzq = True
        exponente = self._exponenteestandarIEEE64bits(numero)
        mantisa = self._mantisaestandarIEEE64bits(numero)
        return signo, exponente, mantisa

    def _exponenteestandarIEEE64bits(self, numero):
        posPunto = 0
        exponente = 0
        msjError = "Error: No se pudo realizar el calculo | Conversion._exponenteestandarIEEE64bits(numero)"
        try:
            for i in range(0, len(numero)):
                if numero[i] != '.':
                    posPunto += 1
                else:
                    posPunto -= 1
                    break
            exponente = posPunto + 1023
            exponente = self.decimal_a(exponente, 2)
            return exponente
        except:
            print(msjError)
            return None

    def _mantisaestandarIEEE64bits(self, numero):
        mantisa = ""
        msjError = "Error: No se pudo realizar el calculo | Conversion._mantisaestandarIEEE64bits(numero)"
        try:
            mantisa = numero.replace('.', '')
            mantisa = list(mantisa)
            while len(mantisa[1:]) < 52:
                mantisa.append('0')
            mantisa = "".join(list(mantisa)[1:53])
            return mantisa
        except:
            print(msjError)
            return None

    def IEEE32Bits_a_decimal(self, signo, exponente, mantisa):
        final = -1
        exp = ""
        base = ""
        decimal = ""
        numero = ""
        exponente = list(exponente)
        mantisa = list(mantisa)
        while len(exponente) < 8:
            exponente.append('0')
        while len(mantisa) < 23:
            mantisa.append('0')
        exponente = "".join(exponente)
        mantisa = "".join(mantisa)
        if signo == "0" :
            final = final * -1
        exp = self.binario_a_decimal(exponente) - 127
        mts = '1' + mantisa
        base = mts[0:int(exp) + 1]
        decimal = mts[int(exp) + 1:]
        numero = self.binario_a_decimal(base + "." + decimal) * final
        return str(numero)

    def IEEE64Bits_a_decimal(self, signo, exponente, mantisa):
        final = -1
        exp = ""
        base = ""
        decimal = ""
        numero = ""
        exponente = list(exponente)
        mantisa = list(mantisa)
        while len(exponente) < 11:
            exponente.append('0')
        while len(mantisa) < 52:
            mantisa.append('0')
        exponente = "".join(exponente)
        mantisa = "".join(mantisa)
        if signo == "0":
            final = final * -1
        exp = self.binario_a_decimal(exponente) - 1023
        mts = '1' + mantisa
        base = mts[0:int(exp) + 1]
        decimal = mts[int(exp) + 1:]
        numero = self.binario_a_decimal(base + "." + decimal) * final
        return str(numero)





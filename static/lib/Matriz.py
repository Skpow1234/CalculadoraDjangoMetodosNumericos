import numpy as np
import scipy.linalg as la
from static.lib.Utilidad import Utilidad

def suma(mA, mB):
  R = None
  if type(mA) == type(mB):
    if mA.shape[0] == mB.shape[0] and mA.shape[1] == mB.shape[1]:
      R = mA+mB
  else:
    R = mA+mB
  return R


def resta(mA, mB):
  R = None
  if type(mA) == type(mB):
    if mA.shape[0] == mB.shape[0] and mA.shape[1] == mB.shape[1]:
      R = mA-mB
  else:
    R = mA-mB
  return R


def multiplicacion(mA, mB):
  R = None
  if mA.shape[1] == mB.shape[0]:
    R = np.dot(mA, mB)
  return R

def division(mA, mB):
  R = None
  if type(mA) == type(mB):
    if mA.shape[1] == mB.shape[0]:
      R = mA/mB
  else:
    R = mA/mB
  return R

def gauss_jordan(mA, mB):
  x = None
  x = np.linalg.solve(mA, mB)
  return x

def escalar(mA, escalar):
    R = (mA)*escalar
    return R


def elevacion(mA, n):
  resultado = mA
  for x in range(1, n):
    resultado = np.dot(resultado, mA)
  return resultado

#UNA MATRIZ


def transpuesta(mA):
  return np.transpose(mA)


def determinante(mA):
  try:
    return round(np.linalg.det(mA))
  except:
    return None


def inversa(mA):
  try:
    return np.linalg.inv(mA)
  except:
    return None


def rango(mA):
  return np.linalg.matrix_rank(mA)


def triangular(mA):
  T = np.copy(mA)
  row, col = T.shape
  for r in range(1, row):
    pivote = T[r, 0]
    for c in range(0, col):
      T[r, c] = T[r, c]-(T[0, c]*pivote)
  if row > 2:
    counter = 2
    while counter < row:
      for r in range(counter, row):
        pivote = T[r, counter-1]/T[counter-1, counter-1]
        for c in range(counter-1, col):
          T[r, c] = T[r, c]-T[counter-1, c]*pivote
      counter += 1
  return T


def factorizacionLU(mA):
  T = np.copy(mA)
  row, col = mA.shape
  L = np.zeros(mA.shape)
  U = triangular(mA)
  for r in range(0, row):
    for c in range(0, col):
      if(r == c):
        L[r, c] = 1
      if(r < c):
        pivote = (T[c, r]/T[r, r])
        L[c, r] = pivote
        for k in range(0, row):
          T[c, k] -= (pivote*T[r, k])
  return L, U

#AJUSTE DE CURVAS
def elevar(datos, exp):
    for i in range(len(datos)):
        datos[i] = datos[i]**exp 
    return datos

def multiplicar(datos, datos2):
    resultado = []
    for i in range(len(datos)):
        resultado.append(datos[i]*datos2[i])
    return resultado

def sumatoria(inicio, fin, datos):
    suma = 0
    for i in range(inicio, fin):
        suma += datos[i]
    return suma

def ajuste_curvas(mA):
    n = mA[0].size
    exponente = 1
    grados = [2, 3, 4, 5, 6, 7]
    matrizSoluciones = []
    resultado = []
    for grado in grados:
        matriz = np.zeros((grado,grado), float)
        matrizSolucion = np.zeros((matriz.shape[0], 1), float)
        for fil in range(matriz.shape[0]):
            exponente = fil
            for col in range(matriz.shape[1]):
                if fil == 0 and col == 0:
                    matriz[fil][col] = n
                else:
                    matriz[fil][col] = sumatoria(0, n, elevar(mA[0].copy(), exponente))
                exponente += 1
        exponente = 0
        for fil in range(matrizSolucion.shape[0]):
            if fil == 0:
                matrizSolucion[fil] = sumatoria(0, n, mA[1])
            else:
                matrizSolucion[fil] = sumatoria(0, n, multiplicar(elevar(mA[0].copy(), exponente), mA[1].copy()))
            exponente += 1
        try:
          resultado = Utilidad.redondear_matriz(gauss_jordan(matriz, matrizSolucion))
        except:
          resultado = []
        if len(resultado) > 0:
          formula = ""
          iterador = len(resultado) - 1
          while iterador >= 0:
              if resultado[iterador] >= 0 and iterador < len(resultado) - 1:
                  formula += "+"
              if iterador == 0:
                  formula += f"{resultado[iterador][0]}"
              elif iterador == 1:
                  formula += f"{str(resultado[iterador][0])}x"
              else:
                  formula += f"{str(resultado[iterador][0])}x^{iterador}"
              iterador -= 1
          matrizSoluciones.append([f"Grado {str(grado - 1)}", formula])
    matrizSoluciones = np.array(matrizSoluciones)
    return matrizSoluciones
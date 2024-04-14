import numpy as np
from hlf_variables import DIMENSION_TABLERO

def generar_coordenada_aleatoria():
    letras = 'ABCDEFGHIJ'
    x = np.random.randint(0, DIMENSION_TABLERO)
    y = np.random.randint(0, DIMENSION_TABLERO)
    return letras[x] + ' ' + str(y + 1)

def validar_coordenada(coordenada):
    letras = 'ABCDEFGHIJ'
    if len(coordenada) < 2:
        return False
    if coordenada[0].upper() not in letras:
        return False
    if not coordenada[1:].isdigit():
        return False
    if int(coordenada[1:]) < 1 or int(coordenada[1:]) > DIMENSION_TABLERO:
        return False
    return True

def juego_terminado(tablero):
    return np.sum(tablero.tablero) == 0
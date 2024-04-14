import numpy as np
from hlf_variables import DIMENSION_TABLERO, BARCOS

class Tablero:
    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
        self.dimensiones = (DIMENSION_TABLERO, DIMENSION_TABLERO)
        self.barcos = BARCOS
        self.tablero = np.zeros(self.dimensiones, dtype=int)
        self.tablero_disparos = np.zeros(self.dimensiones, dtype=int)

    def colocar_barco(self, x, y, eslora, orientacion):
        if orientacion == 'horizontal':
            for i in range(eslora):
                self.tablero[x + i, y] = 1
        elif orientacion == 'vertical':
            for i in range(eslora):
                self.tablero[x, y + i] = 1

    def colocar_barcos(self):
        for barco, eslora in self.barcos.items():
            colocado = False
            while not colocado:
                x = np.random.randint(0, DIMENSION_TABLERO)
                y = np.random.randint(0, DIMENSION_TABLERO)
                orientacion = np.random.choice(['horizontal', 'vertical'])
                if self.validar_posicion_barco(x, y, eslora, orientacion):
                    self.colocar_barco(x, y, eslora, orientacion)
                    colocado = True

    def validar_posicion_barco(self, x, y, eslora, orientacion):
        if orientacion == 'horizontal':
            if x + eslora > DIMENSION_TABLERO:
                return False
            for i in range(eslora):
                if self.tablero[x + i, y] != 0:
                    return False
        elif orientacion == 'vertical':
            if y + eslora > DIMENSION_TABLERO:
                return False
            for i in range(eslora):
                if self.tablero[x, y + i] != 0:
                    return False
        return True

    def disparo_coordenada(self, coordenada):
        x, y = self.letras_coordenada(coordenada)
        if self.tablero[x, y] == 1:
            print("Tocado!")
            self.tablero_disparos[x, y] = 1
            if self.barco_hundido(x, y):
                print("Barco hundido!")
        else:
            print("Agua!")
            self.tablero_disparos[x, y] = -2

    def barco_hundido(self, x, y):
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                cont = 0
                nx, ny = x, y
                while 0 <= nx < DIMENSION_TABLERO and 0 <= ny < DIMENSION_TABLERO and self.tablero[nx, ny] == 1:
                    cont += 1
                    nx += dx
                    ny += dy
                if cont == 0:
                    continue
                elif cont == 1:
                    return True
                elif cont > 1:
                    return False

    def letras_coordenada(self, coordenada):
        letras = 'ABCDEFGHIJ'
        x = letras.index(coordenada[0].upper())
        y = int(coordenada[1:]) - 1
        return x, y

    def imprimir_tablero(self):
        print("Tablero de", self.id_jugador)
        print("  ", "  ".join(str(i) for i in range(1, DIMENSION_TABLERO + 1)))
        letras = 'ABCDEFGHIJ'
        for i in range(DIMENSION_TABLERO):
            row = ''.join(str(cell) for cell in self.tablero_disparos[i])
            print(letras[i], row.replace('0', ' - ').replace('1', ' X ').replace('-2', ' O ')) 
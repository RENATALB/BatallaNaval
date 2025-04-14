import random #Para que se hagan barcos en lugares random, hay que usar la funcion random.randint

"""
Tablero: N*N
Persona vs computadora
10 disparos
5 barcos
"""

CANTIDAD_DISPAROS:int = 10
CANTIDAD_BARCOS:int = 5 
TAMAÑO_TABLERO = int(input("Tamaño tablero: "))


#Se pone false ya que no hay nada ahi, es el predeterminado del tablero
tablero:list = [[False for _ in range(TAMAÑO_TABLERO)] for _ in range(TAMAÑO_TABLERO)]

for fila in (tablero):
    print(fila)

x = int(input("X: ")) #Este input no puede estar suelto, deberia estar en el bucle FOR porque se repite
y = int(input("Y: ")) #Este input no puede estar suelto, deberia estar en el bucle FOR porque se repite

def generadorBarcos(tablero, CANTIDAD_BARCOS):
    barcosPosicionados:int = 0
    while barcosPosicionados <= CANTIDAD_BARCOS:
        x = random.randint(0, TAMAÑO_TABLERO - 1)
        y = random.randint(0, TAMAÑO_TABLERO - 1)
        if tablero [x] [y]
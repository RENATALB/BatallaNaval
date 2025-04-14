import random

CANTIDAD_DISPAROS = 10
CANTIDAD_BARCOS = 5
TAMAÑO_TABLERO = 5

#Se pone false ya que no hay nada ahi
tablero = [[False for _ in range(TAMAÑO_TABLERO)] for _ in range(TAMAÑO_TABLERO)]

for fila in (tablero):
    print(fila)

#crear una funcion que reciba al tablero y cree barcos al azar (usando random.randint)
#hay que probar si anda, yo creo que si pero al faltar otra parte del codigo no se
def posicion_barcos(tablero, CANTIDAD_BARCOS):
    colocados = 0
    while colocados < CANTIDAD_BARCOS: #mientras que los barcos colocados sean menos de 6

        fila = random.randint(0, TAMAÑO_TABLERO - 1)
        columna = random.randint(0, TAMAÑO_TABLERO - 1)
        # pongo -1 ya que 0 a 5 (como dice tamaño_tablero = 5) en realidad, serian 6, 
        # entonces si le restamos 1 serian 5
        
        if not tablero[fila][columna]:
            tablero[fila][columna] = True
            #si no hay nada en esa casilla, entonces se coloca un barco y se vuelve true

            colocados += 1 
            #se le suma un colocado hasta llegar al menor mas alto de CANTIDAD_BARCOS (o sea, 4)
            #sino ejecutamos esta linea, el bucle se repitiria por siempre

posicion_barcos(tablero, CANTIDAD_BARCOS)

for fila in (tablero):
    print(fila)
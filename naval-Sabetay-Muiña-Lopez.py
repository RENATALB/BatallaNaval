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



def generadorBarcos(tablero, CANTIDAD_BARCOS): # Esta función es para posicionar de manera aleatoria los barcos que se deben adivinar
    barcosPosicionados:int = 0
    while barcosPosicionados < CANTIDAD_BARCOS:
        x = random.randint(0, TAMAÑO_TABLERO - 1)
        y = random.randint(0, TAMAÑO_TABLERO - 1)
        if not tablero [x] [y]:
            tablero [x] [y] = True # Si esta casilla del tablero no está ocupada, se pone el barco y se convierte en true
            barcosPosicionados += 1

generadorBarcos(tablero, CANTIDAD_BARCOS)

aciertos:int = 0
fallos:int = 0

for disparos in range(1, CANTIDAD_DISPAROS + 1):
    x = int(input("X: ")) - 1 #Este input no puede estar suelto, deberia estar en el bucle FOR porque se repite
    y = int(input("Y: ")) - 1 #Este input no puede estar suelto, deberia estar en el bucle FOR porque se repite
    if tablero [x] [y]:
        print("¡Barco hundido!💥")
        aciertos += 1
        tablero [x] [y] = False
    else:
        print("No hay barcos en esta posición 💧")
        fallos += 1

print("Juego terminado")
print("Aciertos: {aciertos}")
print("Fallos: {fallos}")
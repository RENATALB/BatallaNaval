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
    x = int(input("X: ")) - 1
    y = int(input("Y: ")) - 1
    if tablero[x][y] == True:  # Si hay un barco en la casilla
        print("¡Barco hundido!💥")
        aciertos += 1
        tablero[x][y] = "💥"  # Marcar como barco hundido
        if aciertos == CANTIDAD_BARCOS:
            print("¡Todos los barcos han sido hundidos! 🎉")
            break
    elif tablero[x][y] == False:  # Si no hay nada en la casilla
        print("No hay barcos en esta posición 💧")
        tablero[x][y] = "💧"  # Marcar como agua
        fallos += 1
    else:
        print("Ya disparaste en esta posición.")

# Imprimir el tablero con los emojis correspondientes
for fila in tablero:
    print(" ".join(
        "💥" if casilla == "💥" else  # Barco hundido
        "💧" if casilla == "💧" else  # Agua
        "🚢" if casilla == True else  # Barco no hundido
        "💧"  # Agua por defecto
        for casilla in fila
    ))  #Estas últimas lineas de código nos ayudó CoPilot para reemplazar los true y false por emojis

print("Juego terminado")
print(f"Aciertos: {aciertos}")
print(f"Fallos: {fallos}")
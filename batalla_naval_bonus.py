#barcos en una sola coordenada, no tienen tamaño
#ESTE NO ES EL ARCHIVO DE BONUS DEFINITIVO, HAY QUE CAMBIAR COSAS
#TODO: lista de lista booleana, que las coordenadas no sean de 0-7 sino 1-8, ver lo de constantes
#FIXME: LPM ES UN QUILOMBO ESTE ARCHIVO ME ACABO DE AVIVAR

TAMAÑO = int(input("Tamaño tablero: "))
NUM_BARCOS = 3 #cantidad de barcos por jugador

#tablero vacio, lista de listas. Cada "O" representa una celda del mar
def crear_tablero(tamaño):
    return [["O"] * tamaño for _ in range(tamaño)]


#Muestra cada fila del tablero en consola. join(fila) convierte una lista como ["O", "X", "O"] en una línea "O X O".
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))


# Se le pide al jugador que ponga coordenadas y tmb se valida de que no sea invalido o fuera del tablero
def colocar_barcos(jugador):
    print(f"\n{jugador}, coloca tus {NUM_BARCOS} barcos.")
    barcos = []
    while len(barcos) < NUM_BARCOS:
        try:
            fila = int(input(f"Fila del barco #{len(barcos)+1} (0-{TAMAÑO-1}): "))
            columna = int(input(f"Columna del barco #{len(barcos)+1} (0-{TAMAÑO-1}): "))

        #Si esta todo bien, se guarda como una TUPLA
            if (0 <= fila < TAMAÑO and 0 <= columna < TAMAÑO):
                if (fila, columna) not in barcos:
                    barcos.append((fila, columna))
                else:
                    print("Ya colocaste un barco ahí.")
            else:
                print("Coordenadas fuera del tablero.")
        except ValueError:
            print("Ingresa números válidos.")
    return barcos

# Se ejecuta cada vez que un jugador dispara
# El parametro disparo registra los tiros del jugador
# El parametro barcos_enemigos tiene las posiciones de los barcos del otro jugador
def turno(jugador, disparos, barcos_enemigos):
    print(f"\nTurno de {jugador}")
    mostrar_tablero(disparos)
    # Valida si el disparo es dentro del tablero o es invalido, o si ya disparó
    while True:
        try:
            fila = int(input("Adivina fila: "))
            columna = int(input("Adivina columna: "))
            if not (0 <= fila < TAMAÑO and 0 <= columna < TAMAÑO):
                print("Fuera de rango.")
                continue
            if disparos[fila][columna] != "O":
                print("Ya disparaste ahí.")
                continue
            break
        except ValueError:
            print("Coordenadas inválidas.")


    if (fila, columna) in barcos_enemigos:
        disparos[fila][columna] = "🎯"
        barcos_enemigos.remove((fila, columna)) # si adivina, elimina el barco
        print("🔥 ¡Tocado!")
        if not barcos_enemigos:
            print("💥 ¡Todos los barcos enemigos han sido hundidos!") #si no hay barcos, hace return True para ejecutar el bucle while y terminar el juego
            return True
    else:
        disparos[fila][columna] = "🌊"
        print("💦 Agua.") #si no adivina, return False hace que alterne el turno
    return False

# bucle principal, donde se guardan las coordenadas del jugador 1 o 2,
# se alternan los turnos,
# se limpian los inputs con print("\n" * 30)
def jugar():
    print("=== JUGADOR 1 ===")
    barcos1 = colocar_barcos("Jugador 1")
    print("\n" * 30)

    print("=== JUGADOR 2 ===")
    barcos2 = colocar_barcos("Jugador 2")
    print("\n" * 30)

    disparos1 = crear_tablero(TAMAÑO)
    disparos2 = crear_tablero(TAMAÑO)

    turno_actual = 1

    # si un jugador hunde todos los barcos enemigos, el juego termina con un break
    while True:
        if turno_actual == 1:
            if turno("Jugador 1", disparos1, barcos2):
                print("🎉 ¡Jugador 1 gana!")
                break
            turno_actual = 2
        else:
            if turno("Jugador 2", disparos2, barcos1):
                print("🎉 ¡Jugador 2 gana!")
                break
            turno_actual = 1

if __name__ == "__main__":
    jugar()

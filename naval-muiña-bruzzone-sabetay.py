
TAMAÑO = int(input("Tamaño tablero: "))
NUM_BARCOS = 3  # Cantidad de barcos por jugador

# #tablero vacio, lista de listas. Cada "O" representa una celda del mar
def crear_tablero(tamaño):
    return [["O"] * tamaño for _ in range(tamaño)]

#Muestra cada fila del tablero en consola. join(fila) convierte una lista como ["O", "X", "O"] en una línea "O X O".
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

# Se le pide al jugador que ponga coordenadas y tmb se valida de que no sea invalido o fuera del tablero
def colocar_barcos(jugador):
    print(f"\n{jugador}, colocá tus {NUM_BARCOS} barcos.")
    barcos = []
    while len(barcos) < NUM_BARCOS: 
    #le tuve que preguntar a CHATGPT de arreglar esto y porque tenia que poner len(barcos) en vez de solo barcos.
    # me dijo que Comparar una lista directamente con un número (barcos < NUM_BARCOS) no tiene sentido en Python y va a tirar un error como: TypeError: '<' not supported between instances of 'list' and 'int'
    # En cambio, poner len(barcos) dice cuantos barcos (coordenadas) ya hay. Por ejemplo: len([(0,2), (1,4)]) → 2. Y eso sí se puede comparar con NUM_BARCOS porque ambos son números.

        try:
            fila = int(input(f"Fila del barco #{len(barcos)+1} (1-{TAMAÑO}): ")) - 1
            columna = int(input(f"Columna del barco #{len(barcos)+1} (1-{TAMAÑO}): ")) - 1
            
            #Si esta todo bien, se guarda como una TUPLA
            if 0 <= fila < TAMAÑO and 0 <= columna < TAMAÑO:
                if (fila, columna) not in barcos:
                    barcos.append((fila, columna))
                else:
                    print("⚠️ Ya colocaste un barco ahí.")
            else:
                print("⛔ Coordenadas fuera del tablero.")
        except ValueError:
            print("❌ Ingresá números válidos.")
    return barcos

# cuando El jugador realiza un disparo
#El parametro disparo registra los tiros del jugador
# El parametro barcos_enemigos tiene las posiciones de los barcos del otro jugador
#el parametro stats guarda las estadisticas para mostrarlas dsp en pantalla
def turno(jugador, disparos, barcos_enemigos, stats):
    print(f"\n🎮 Turno de {jugador}")
    mostrar_tablero(disparos)

# Valida si el disparo es dentro del tablero o es invalido, o si ya disparó
    while True:
        try:
            fila = int(input("Adiviná fila: ")) - 1
            columna = int(input("Adiviná columna: ")) - 1

            if not (0 <= fila < TAMAÑO and 0 <= columna < TAMAÑO):
                print("⛔ Fuera de rango.")
                continue
            if disparos[fila][columna] != "O":
                print("⚠️ Ya disparaste ahí.")
                continue
            break
        except ValueError:
            print("❌ Coordenadas inválidas.")

    if (fila, columna) in barcos_enemigos:
        disparos[fila][columna] = "🎯"
        stats["aciertos"] += 1
        barcos_enemigos.remove((fila, columna)) # si adivina, elimina el barco
        print("🔥 ¡Tocado!")
        if not barcos_enemigos:
            print("💥 ¡Todos los barcos enemigos fueron hundidos!") #si no hay barcos, hace return True para ejecutar el bucle while y terminar el juego
            return True
    else:
        disparos[fila][columna] = "🌊"
        stats["fallos"] += 1
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

    # Tableros de disparos de cada jugador
    disparos1 = crear_tablero(TAMAÑO)
    disparos2 = crear_tablero(TAMAÑO)

    # Estadísticas por jugador
    stats1 = {"aciertos": 0, "fallos": 0}
    stats2 = {"aciertos": 0, "fallos": 0}

    turno_actual = 1

    # si un jugador hunde todos los barcos enemigos, el juego termina con un break
    while True:
        if turno_actual == 1:
            if turno("Jugador 1", disparos1, barcos2, stats1):
                print("\n🎉 ¡Jugador 1 gana!")
                break
            turno_actual = 2
        else:
            if turno("Jugador 2", disparos2, barcos1, stats2):
                print("\n🎉 ¡Jugador 2 gana!")
                break
            turno_actual = 1

    # Mostrar resultados finales
    print("\n=== RESULTADOS FINALES ===")

    print(f"\nJugador 1:\n Aciertos: {stats1['aciertos']} | Fallos: {stats1['fallos']}")
    print("Tablero de disparos del Jugador 1:")
    mostrar_tablero(disparos1)

    print(f"\nJugador 2:\n Aciertos: {stats2['aciertos']} | Fallos: {stats2['fallos']}")
    print("Tablero de disparos del Jugador 2:")
    mostrar_tablero(disparos2)

# Inicia el juego
if __name__ == "__main__":
    jugar()

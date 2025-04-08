Con lo visto en clase sobre listas de listas, armar un programa que simule un juego de "Batalla Naval".

Dado un tablero de N * N, es decir una lista de N listas de N elementos cada una, donde cada elemento puede contener o no un barco, el programa debe permitir ingresar las coordenadas de disparo, y mostrar si se acertó o no en un barco. Para este ejemplo N=10 pero deberia poder cambiar el tamaño del tablero en función de N.

Para esta primera consigna, los barcos se asignan por código. Opcionalmente se pueden ubicar en posiciones al azar. Los barcos ocupan una sola casilla

El usuario tiene una cantidad predefinida de disparos, esto es, una cantidad de intentos para acertar en los barcos.

Al finalizar el juego, mostrar la cantidad de disparos acertados y fallados, y como finaliza el tablero (los barcos que quedaron en pie).

Recomendaciones:

Implementar el tablero como una List[List[Bool]], de esta forma las coordenadas del tablero serán tablero[fila][columna].
Utilizar constantes para definir la cantidad de disparos y la cantidad de barcos.

⚡️ Bonus
Dada una variable que determine la cantidad de barcos, modificar el programa para permitirle a otro usuario ingresar previamente las posiciones de los N barcos.

Permitir jugar de a 2 jugadores, y que, por turnos cada uno pueda disparar contra el tablero del otro.

Permitir barcos de hasta 3 casillas.

ENTREGAR EL CODIGO COMENTADO Y QUE TENGA TYPEHINTS. Y SI USAMOS IA O CUALQUIER OTRO DOCS HAY QUE ENTREGARLO TAMBIEN.
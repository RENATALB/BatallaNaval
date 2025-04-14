import random #para que se hagan barcos en lugares random, hay que usar la funcion random.randint

tablero = [] #el tablero al ser una lista de listas bool, no puede estar vacia

CANTIDAD_DISPAROS: int = 10
CANTIDAD_BARCOS: int = 5 # Puse la variable en mayuscula para yo entender que es una constante
"""
Tablero: 5x5
Persona vs computadora
10 disparos
5 barcos
"""


x = int(input("X: ")) #Este input no puede estar suelto, deberia estar en el bucle FOR porque se repite
y = int(input("Y: ")) #Este input no puede estar suelto, deberia estar en el bucle FOR porque se repite
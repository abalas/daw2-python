"""Escribir un programa que nos permita generar una quiniela. Para ello nos debe generar
quince números aleatorios entre el 1 y el 3. Recuerda que los resultados válidos son 1 X o 2,
así que si te sale un 3 lo que tienes que imprimir en pantalla es una X"""

import random
numAle = 0
for i in range(0,15):
    numAle = random.randint(0, 3)
    if numAle == 3:
        print("X",end="")
    else:
        print(numAle,end="")
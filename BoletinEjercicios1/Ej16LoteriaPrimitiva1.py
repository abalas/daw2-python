import random
""" Escribir un programa que genere seis números aleatorios entre el 1 y el 49 (simulando una
lotería primitiva). Por el momento no te preocupes de que algunos números puedan salir
repetidos. Ya resolveremos eso más adelante."""
numeroLoteria = ""
for i in range(0, 6):
    numeroLoteria += str(random.randint(0,50))
print(numeroLoteria)
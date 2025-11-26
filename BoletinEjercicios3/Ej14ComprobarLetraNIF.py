"""Hay que sumar las ocho cifras y dividirla por 23 y qudarnos con el resto
nos saldrá un numero entre 0 y 22 """

import re
def calcularLetra(n):
    """suma =0
    for i in cadena:
        suma += int(i) esto fua un malentendido por mi parte asi no se hace"""
    numero=int(n)%23
    equivalencia = "TRWAGMYFPDXBNJZSQVHLCKE"
    return equivalencia[numero]
nif = input("Introduce el NIF: ").upper()
patron=r"^[0-9]{8}[A-Za-z]$"



if re.match(patron, nif):
    print(nif[0:8])
    if calcularLetra(nif[0:8]) == nif[8]:
        print("Es válido")
    else:
        print("La letra final esta mal :D")
else:
    print("No es válido")


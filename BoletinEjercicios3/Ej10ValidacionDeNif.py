"""Escribe un programa que valide si un NIF español introducido por teclado es correcto.
La longitud exacta de la cadena ha de ser de 9 caractéres. Los ocho primeros han de
ser números comprendidos entre el 0 y el 9 y el último una letra que puede estar
escrita en mayúsculas o minúsculas."""
import re
nif = input("Introduce el NIF: ")
patron=r"^[0-9]{8}[A-Za-z]$"


if re.match(patron, nif):
    print("Es válido")
else:
    print("No es válido")


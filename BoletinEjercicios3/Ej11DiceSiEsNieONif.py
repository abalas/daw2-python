""" Mejorar el programa anterior para que detecte si se trata de un NIF o un NIE y nos
comunique, además de si es válido de que tipo es. Un NIE es una cadena de 9 caractéres que siempre empieza por X,Y o Z y a
continuación vienen 7 cifras y una letra final. Las letras inicial y final pueden estar
escritas con mayúsculas o con minúsculas"""
import  re
import re
input = input("Introduce el NIF o NIE: ")
patron=r"^[0-9]{8}[A-Za-z]$"
patronNIE=r"[X-Zx-z][0-9]{7}[A-Za-z]"
if re.fullmatch(patron, input):
    print("Es un NIF")
else:
    if re.fullmatch(patronNIE, input):
        print("Es un NIE")
    else:
        print("No es válido")

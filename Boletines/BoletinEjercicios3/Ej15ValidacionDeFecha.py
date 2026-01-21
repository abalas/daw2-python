"""Escribe un programa que reciba por teclado una fecha en el formato DD/MM/YYYY. El
programa debe de comprobar si la fecha es correcta teniendo en cuenta:
Qué el formato sea el correcto
Que la fecha sea totalmente válida teniendo en cuenta incluso los años que son
bisiestos (aquellos que son divisibles entre cuatro)."""
import re
fecha = input("Introduce una fecha: ")
patron = r"[0-31]"
if re.fullmatch(patron, fecha):
    print("Es valido")
else:
    print("No es valido")

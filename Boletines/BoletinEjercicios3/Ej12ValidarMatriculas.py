"""Las matrículas españolas constan de un número de cuatro dígitos y tres letras
cualesquiera en mayúsculas a excepción de las vocales, la Ñ y la Q. Escribe un
programa que detecte si una matrícula introducida por teclado es válida o no."""
import re
matriculaValida = False
patron = r"[0-9]{4}[B-DF-HJ-NP-TV-Z]{3}"
while not matriculaValida:
    matricula = input("Introduzca su matricula: ").upper()
    if re.fullmatch(patron,matricula):
        matriculaValida = True
        print("Matricula valida")
    else:
        print("Matricual inválida")
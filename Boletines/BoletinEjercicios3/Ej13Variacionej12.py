""". Modifica el programa anterior contemplando que entre los números y las letras
podría haber un espacio en blanco (uno solo) o un guión. En ambos casos se
considerará también que la matrícula es válida (si cumple todo lo demás, claro)"""

import re
matriculaValida = False
patron = r"[0-9]{4}[ -][B-DF-HJ-NP-TV-Z]{3}"
while not matriculaValida:
    matricula = input("Introduzca su matricula: ").upper()
    if re.fullmatch(patron,matricula):
        matriculaValida = True
        print("Matricula valida")
    else:
        print("Matricual inválida")
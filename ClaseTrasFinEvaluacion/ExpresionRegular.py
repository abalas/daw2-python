import re
patron=r"[6-8][0-9]{8}"
num1="655112233"
num2="913345555"

if re.match(patron, num1):
    print("num1 es un telefóno móvil")
else:
    print("num1 No es un telédfono móvil")
if re.match(patron, num2):
    print("num2 es un telefóno móvil")
else:
    print("num2 No es un telédfono móvil")



""""
match: valida al principio
search: lo busca dentro de la cadena
fullmatch: mas util
"""
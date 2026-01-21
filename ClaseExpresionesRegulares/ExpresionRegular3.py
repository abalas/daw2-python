import re
patron=r"[^579]"
num1="655112233"
num2="913345555"

if re.match(patron, num1):
    print("Es válido")
else:
    print("No es válido")




""""
^ Acento circunflejo frances
match: valida al principio
search: lo busca dentro de la cadena
fullmatch: mas util
"""
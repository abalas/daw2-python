import re
patron=r"[0-9]{4}[\s|-][B-DF-HJL-NPR-TV-Z]{3}"
num1="655112233"
num2="913345555"

if re.match(patron, num1):
    print("Es válido")
else:
    print("No es válido")




""""
match: valida al principio
search: lo busca dentro de la cadena
fullmatch: mas util
"""
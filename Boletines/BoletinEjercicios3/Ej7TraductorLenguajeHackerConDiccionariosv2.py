frase = input("Introduzca una frase")

sust = {"a":"4", "A":"4",
        "o":"0", "O":"0",
        "i":"1", "I":"1",
        "e":"3", "E":"3"}

fraseFinal = ""
partes = []
for c in frase:
    partes.append(sust.get(c, c))
fraseFinal = ''.join(partes)

print(fraseFinal)
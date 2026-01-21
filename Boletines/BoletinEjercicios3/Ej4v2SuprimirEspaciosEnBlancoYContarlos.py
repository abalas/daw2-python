from itertools import count

frase= input("Introduzca una frase:")
contEspacios=frase.count(" ")

fraseSinEspacios=frase.replace(" ","")


print(f"Numero de espacios: {contEspacios}")
print(f"Frase sin espacios: {fraseSinEspacios}")
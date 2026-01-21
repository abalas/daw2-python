import random
frase = input("Introduce una cadena: ")
listaFrase=list(frase)
random.shuffle(listaFrase)
print("Resultado:", "".join(listaFrase))

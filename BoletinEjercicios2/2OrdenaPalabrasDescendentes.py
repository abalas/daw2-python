import array
palabra1 = input("Introduzca una palabra")
palabra2 = input("Introduzca otra palabra")
palabra3 = input("Introduzca otra palabra")

lista = [palabra1, palabra2, palabra3]
lista.sort(reverse=True)
texto=str(lista)
texto = texto.replace("[","")
texto = texto.replace("]","")
print(texto)


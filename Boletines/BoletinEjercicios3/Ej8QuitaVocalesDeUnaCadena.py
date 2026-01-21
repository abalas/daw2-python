"""Escribir un programa que reciba una cadena de texto por teclado y la muestre sin
vocales. Por ejemplo, si recibe la cadena “Hola Mundo” debería de devolver “Hl Mnd”."""

frase = input("Introduzca una frase: ")
fraseSinVocales = ""
vocales = "AaÁáEÉeéIÍíiOÓoóUÚuú"
for i in frase:
    if i in vocales:
        pass
    else:
        fraseSinVocales += i
print(fraseSinVocales)
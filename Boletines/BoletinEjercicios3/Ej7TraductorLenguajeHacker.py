"""Escribir un programa que pida por teclado una cadena de texto y la escriba con el
alfabeto típico de los hackers sustituyendo las letras a por el número 4, las letras e por
el número 3, las letras i por el número 1 y las letras o por el número 0. Considera que
las vocales pueden estar escritas en mayúsculas o minúsculas, pero no hace falta que
tengas en cuenta que además podrían ir acentuadas"""

frase = input("Introduzca una frase")
fraseFinal = frase.replace("a","4" )
fraseFinal = fraseFinal.replace("A","4" )
fraseFinal = fraseFinal.replace("e","3" )
fraseFinal = fraseFinal.replace("E","3")
fraseFinal = fraseFinal.replace("o","0" )
fraseFinal = fraseFinal.replace("O","0")

print(fraseFinal)
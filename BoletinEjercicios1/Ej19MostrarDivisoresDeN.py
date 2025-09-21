"""Escribir un programa que pida un número por teclado y nos muestre sus divisores"""
num = int(input("Introduzca un numero"))

print(f"Divisores de {num}: ", end="")
for i in range(1, int(num/2)):
    if num%i == 0:
        print(f"{i}, ",end="")
num1 = int(input("Introduzca un número: "))
num2 = int(input("Introduzca otro número: "))
num3 = int(input("Introduzca otro número: "))

if num1 <= num2 and num1 <= num3:
    menor = num1
    if num2 <= num3:
        medio = num2
        mayor = num3
    else:
        medio = num3
        mayor = num2
elif num2 <= num1 and num2 <= num3:
    menor = num2
    if num1 <= num3:
        medio = num1
        mayor = num3
    else:
        medio = num3
        mayor = num1
else:
    menor = num3
    if num1 <= num2:
        medio = num1
        mayor = num2
    else:
        medio = num2
        mayor = num1

print("Ordenados:", menor, medio, mayor)
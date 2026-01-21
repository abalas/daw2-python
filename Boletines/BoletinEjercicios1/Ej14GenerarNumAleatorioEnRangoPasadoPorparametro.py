import random
num1 = int(input("Introduzca el numero menor del rango"))
num2 = int(input("Introduzca el numero mayor del rango"))
if num1 < num2:
    numAle = random.randint(num1, num2)
else:
    numAle = random.randint(num2,num1)
print("Numero aleatorio generado: ", numAle)
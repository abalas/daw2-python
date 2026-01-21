""" Realiza un juego en el que debes de acertar un número entre el 1 y el 50 que el
ordenador ha elegido de forma aleatoria. El programa te indicará si has acertado, si te
has pasado o si te has quedado corto. El programa finaliza cuando se acierta o cuando
se superan el número máximo de intentos establecidos en 5."""
import random
ale = random.randint(1,50)
print(ale)
contFallos = 0
numero = 0
while numero!=ale:
    numero = int(input("Introduzca numero del 1 al 50:"))

    if numero==ale:
        print("Enhorabuena, acertastes!!!")
    elif numero>ale :
        print("Te pasastes")
        contFallos += 1
    elif numero<ale:
        print("Te quedastes corto")
        contFallos += 1
print("Nº de intentos fallidos: ", contFallos)
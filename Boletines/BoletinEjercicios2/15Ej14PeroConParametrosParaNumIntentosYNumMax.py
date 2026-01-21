import random

finalizarJuego = True


while finalizarJuego:
    numMax = int(input("Cual quieres que sea el numero maximo que pueda generar?: "))
    ale = random.randint(1, numMax)
    print(ale)
    contFallos = 0
    acertado = False
    limiteFallos = int(input("Cual es el limite de fallos que quieres tener?: "))

    while contFallos < limiteFallos and not acertado:
        numero = int(input(f"Introduzca un número del 1 al {numMax}: "))

        if numero == ale:
            print("¡Enhorabuena, acertaste!")
            acertado = True
        elif numero > ale:
            print("Te pasaste.")
            contFallos += 1
        else:
            print("Te quedaste corto.")
            contFallos += 1

    if not acertado:
        print(f"No has acertado. El número era {ale}.")
    print("Intentos realizados:", contFallos)

    valor = input("¿Quiere volver a jugar? Teclee '1' para continuar: ")
    if valor != "1":
        finalizarJuego = False

print("Gracias por jugar. ¡Hasta luego!")
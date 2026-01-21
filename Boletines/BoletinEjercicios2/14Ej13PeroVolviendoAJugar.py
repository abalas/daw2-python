import random

finalizarJuego = True

while finalizarJuego:
    ale = random.randint(1, 50)
    contFallos = 0
    acertado = False

    while contFallos < 5 and not acertado:
        numero = int(input("Introduzca un número del 1 al 50: "))

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
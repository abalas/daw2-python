import random

numAle = random.randint(0, 100);

numIntroducido = input("Introduzca un número entre el 0 y el 100:")
while numIntroducido != numAle:
    if numIntroducido < 0 or numIntroducido >100:
        print("Error. Numero no valido")
    else:
            numIntroducido = input("Introduzca un número entre el 0 y el 100:")
            if(numIntroducido > 100)
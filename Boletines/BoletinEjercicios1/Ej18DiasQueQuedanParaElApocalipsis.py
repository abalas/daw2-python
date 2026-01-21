"""Escribe un programa que genere números aleatorios entre el 1 y el 1000 sin parar y que sólo
se detenga cuando salga el 666. Los números que ha tenido que generar tu programa hasta
aparecer el 666 son los que restan para el apocalipsis. Tu programa debería de indicarlo con
un mensaje tétrico (¡Faltan 236 días para que se acabe todo! por ejemplo)"""
import random
contadorDeIntentos = 0
numAle = 0;
while numAle!=666:
    numAle = random.randint(1,1001)
    contadorDeIntentos +=1
print("¡Faltan",contadorDeIntentos," días para que se acabe todo!")
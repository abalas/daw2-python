import random
numeroDeDados = int(input("Cual es el numero de dados con el que jugais"))
numeroDeCaras = int(input("Cual es el numero de caras de los dados?"))

for i in range(0,numeroDeDados,1):
    print("Dado",i,": ",random.randint(0, numeroDeCaras))
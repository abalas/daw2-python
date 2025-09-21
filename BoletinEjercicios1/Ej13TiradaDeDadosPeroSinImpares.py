import random
numeroDeDados = int(input("Cual es el numero de dados con el que jugais"))
numeroDeCaras = int(input("Cual es el numero de caras de los dados?"))
while numeroDeCaras%2!=0:
    numeroDeCaras = int(input("Error. Introduzca otro valor que sea par, ya que los datos con numero de caras impares no existe"))

for i in range(0,numeroDeDados,1):
    print("Dado",i,": ",random.randint(0, numeroDeCaras))
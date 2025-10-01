import random
contadorDeTiradas = 0
iguales = False;
while iguales == False:
    ale1 = random.randint(0,6)
    ale2 = random.randint(0,6)
    contadorDeTiradas += 1
    print("La tirada de dados ha salido")
    if ale1 == ale2 :
        iguales = True

print("En tu dado ha salido: ", ale1, " y ", ale2, " han tomado ", contadorDeTiradas, " para que salgan pares" )
import random
contadorDeTiradas = 0
while True:
    ale1 = random.randint(0,6)
    ale2 = random.randint(0,6)
    contadorDeTiradas += 1
    if ale1 == ale2 :
        break;

print("En tu dado ha salido: ", ale1, " y ", ale2, " han tomado ", contadorDeTiradas, " para que salgan pares" )
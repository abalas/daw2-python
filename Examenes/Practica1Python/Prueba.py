import random
def iguales(dados):
    dado1 = dados[0]
    for i in range(0,dados.length()):
        if(dado1== dados[i]):
            pass
        else:
            return False
    return True

nDados = int(input("Introduzca el numero de dados que quieres tirar: "))
dados = []
for i in range(0, nDados):
    dados.append(random.randint(1, 6))
    print(dados)






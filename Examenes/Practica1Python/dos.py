import random
def iguales(dados):
    dado1 = dados[0]
    for i in range(0,len(dados)):
        if(dado1== dados[i]):
            pass
        else:
            return False
    return True

nDados = int(input("Introduzca el numero de dados que quieres tirar: "))
dados = []
for i in range(0, nDados):
    dados.append(str(random.randint(1, 6)))
strDados = " - ".join(dados)
print(strDados)
while not iguales(dados):
    dados = []
    for i in range(0, nDados):
        dados.append(str(random.randint(1, 6)))
    strDados = " - ".join(dados)
    print(strDados)








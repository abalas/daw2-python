
lista = [5,80,76,43,13,5,80,80,13]
#lista = [1,2,3,4,5,6]
numerosRepetidos = []
existeRepetido = False
for i in lista:
    if(lista.count(i) > 1 and  not i in numerosRepetidos):
        numerosRepetidos.append(i)
        existeRepetido = True
if(not existeRepetido):
    print("No hay elemntos repetidos")
else:
    for i in numerosRepetidos:
        print(f"El número {i} aparece {lista.count(i)} veces")

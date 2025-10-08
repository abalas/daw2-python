#listas tuplas conjuntos diccionarios

lista1 =[]
lista2 = list()
lista3 = [2,4,589,33,1,44,6,7,2]   #se pueden tener elementos repetidos
lista4 = ["Eva", "Álvaro", "Sara"]
lista5 = [34, "jose maría", False, "Pérez", [1,5,"DAM"]]

for elemento in lista5:
    print(elemento)
for i in range(0,len(lista5)):
    print(i, "-", lista5[i])
print(lista5[4][2])
matriz=[[1,2,3],[4,5,6],[7,8,9]]
print(matriz[2][0])

lista5 = lista5 + lista3+lista4
print(lista5)

lista3.extend(lista4+lista5)
print(lista3)

listosa = [1,2,3,4,5,6,7,8]
#Append en la ultima posicion
listosa.append(9)
print(listosa)
#Insert delante de la posicion que indiques
listosa.insert(-1, 333)
print(listosa)
elemento = listosa.pop()
print(elemento)
print(lista3)
listosa.remove(333)
print(listosa)

lista9 = [9,6,7,4,2,5,4,3,2,7,12,9,54,67,0]
lista9.sort()
print(lista9)
lista9.sort(reverse=True)
print(lista9)
lista9.append(333)

#Ver si un elemento está en la lista;

if 333 in lista3:
    print("Está en la lista")
else:
    print("Está en la lista")
    print("Aparece", lista9.count(333), "veces")
if 0 in lista3:
    print(lista3.index(0))

texto = "buenas tardes, patata"
listaTexto = list(texto)

texto2 = str(listaTexto)
texto2=texto2.replace("[", "")
texto2=texto2.replace("]", "")
print(texto2)
matriz = [[1,2,3],[4,5,6],[7,8,9]]
vector = str(matriz[1])


listanueva = lista2[::2]
print(listanueva)


import random
alumnos = ["ana", "Pedro", "Juan"]
print(random.choice(alumnos))
print(random.sample(alumnos),4)
random.shuffle(alumnos)
print(alumnos)


#cosas que faltan por dar: comprobacion de formato
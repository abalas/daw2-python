lista = ["Ana", "Veronica", "Luis", "Rafael"]
for nombre in lista:
    print(nombre)
for i in range(0, len(lista)):
    print(i, "-", lista[i])
for i,nombre in enumerate(lista):
    print(i,"-",nombre)



#Como no hacer un duplicado de la lista
num1 = [4]
num2 = num1
num2[0] *= 2
print(num1)

#Como hacer un duplicacdo de una lista
num1 = [4]
num2 = num1.copy()
num2[0] *= 2
print(num1)
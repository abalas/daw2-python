
def esCapicua(cadena):
    n = len(cadena)
    if(n == 1):
        return True;
    if(n%2 == 0):
        slice1 = cadena[0:n//2]
        slice2 = cadena[n//2:]
        if(slice1==slice2):
            return True;
        else:
            return False;
    else:
        n = n-1
        slice1 = cadena[0:n//2]
        slice2 = cadena[n//2+1:]
        if (slice1 == slice2):
            return True;
        else:
            return False;




numero1 = int(input("Introduzca un numero: "))
numero2 = int(input("Introduzca otro numero: "))
menor = 0
mayor = 0
lista = []
diferencia = 0
if(numero1<numero2):
    menor = numero1
    mayor = numero2
else:
    mayor = numero1
    menor = numero2
if(numero1==numero2):
    pass
else:
    diferencia = mayor - menor
if diferencia==0:
    if(esCapicua(str(numero1))):
        print(f"Numeros capicuas entre {numero1} y {numero2}: {numero1}")
    else:
        print(f"No hay ningún número capicúa entre {numero1} y {numero2}")
else:
    for i in range(menor, mayor+1):
        if(esCapicua(str(i))):
            lista.append(str(i))
    if len(lista)==0:
        print(f"No hay ningún número capicúa entre {menor} y {mayor}")
    else:
        cadenLista = ", ".join(lista)
        print("Numeros capicuas entre ",menor," y ",mayor,":",cadenLista)





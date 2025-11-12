def devolverCodigo(n):
    cadena = list("XXXXXXXXXX")

    if (n == 0):
        cadena[9]="0"
    else:
        cadena[n-1]="0"
    return "".join(cadena)

numero= input("Introduzca un numero de cuatro cifras: ")
while(len(numero) != 4 or not(numero.isdigit())):
    numero= input("Introduzca un numero de cuatro cifras: ")
for i in range(4):
    print(devolverCodigo(int(numero[i])))



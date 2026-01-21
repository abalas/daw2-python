def esPrimo(num):
    for i in range(2,(num//2+1)):
        if num <= 1:
            return False
        if(num%i==0):
            return False
    return True

numero = int(input("Introduzca un numero: "))
if ( esPrimo(numero)):
    print(numero, " es primo.")
else:
    print(numero, " no es primo.")

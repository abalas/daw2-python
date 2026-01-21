"""Queremos ahora hacer un programa que reciba un número por teclado y nos muestre
en orden todos los números de la sucesión de fibonacci que sean menores o iguales
al que has enviado como argumento. Por ejemplo, si metemos el número 4 nos
debería de devolver esto:
0,1,1,2,3"""
numero = int("Introduzca un numero: ")
def calcularSucesionDeFibonacci(numero):
    cadena = ""
    if(numero==1):
        cadena = "0"
    if(numero==2):
        cadena = "0,1"
    if(numero > 2):
        cadena = "0,1"
        a=0
        b=1
        c=1
        aux = c
        for i in range(0,numero-2):
            aux = c
            a = b
            b=c
            c = a + b
            cadena += f",{aux}"

    return cadena

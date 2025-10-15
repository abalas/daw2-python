n = int(input("Introduzca un numero: "))


def imprimirDivisores(n):
    print("1, ",end="")
    for i in range(2,(n/2)+1):
        if n%i==0:
            print("1, ",end="")

imprimirDivisores(n)
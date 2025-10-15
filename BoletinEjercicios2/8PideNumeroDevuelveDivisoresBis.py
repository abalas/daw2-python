n = int(input("Introduzca un numero: "))


def imprimirDivisores(n):
    divisores = []
    for i in range(2,n+1):
        if n%i==0:
            divisores.append(str(i))
    divisores = ", ".join(divisores)
    print(divisores)

imprimirDivisores(n)
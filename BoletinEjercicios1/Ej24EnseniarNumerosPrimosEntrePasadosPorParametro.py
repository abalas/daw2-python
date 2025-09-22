import random
n1 = int(input("Introduce el rango inferior"))
n2 = int(input("Introduce el rango superior"))
def esPrimo(num):
    for i in range(2,(num//2+1)):
        if num <= 1:
            return False
        if(num%i==0):
            return False
    return True
for i in range(n1,n2+1):
    if(esPrimo(i)):
        print(i)
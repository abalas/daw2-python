import random

def esPrimo(num):
    for i in range(2,(num//2+1)):
        if num <= 1:
            return False
        if(num%i==0):
            return False
    return True

nAle = random.randint(50000000, 100000000)
while not (esPrimo(nAle)):
    nAle = random.randint(50000000, 100000000)
print(nAle)
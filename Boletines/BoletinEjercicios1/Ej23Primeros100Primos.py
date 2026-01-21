import random

def esPrimo(num):
    for i in range(2,(num//2+1)):
        if num <= 1:
            return False
        if(num%i==0):
            return False
    return True
for i in range(1,101):
    if(esPrimo(i)):
        print(i)
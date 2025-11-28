"""Escribir un programa que pida un número por teclado y calcule su factorial. Como
sabes, la factorial de un número se calcula multiplicando ese número por los
sucesivos factores que obtenemos restando uno hasta llegar a la unidad. Por ejemplo,
el factorial de 6 (que se representa así 6!) sería este:
6! = 6*5*4*3*2*1 = 720"""

def calcularFactorial( numero):
    factorial = 1
    for i in range (1,numero):
        factorial+= i*factorial
    return factorial


numero = int(input("Introduce un numero"))
print(f"El factorial de  {numero} es {calcularFactorial(numero)}")
"""En matemáticas, la sucesión de Fibonacci se trata de una serie infinita de números
naturales. Los dos primeros son siempre el 0 y el 1. Los siguientes se obtienen
sumando los dos anteriores. El tercero sería 1 (la suma de 0 + 1), el cuarto sería 2 (la
suma de 1 + 1), el quinto 3 (la suma de 1 + 2) y así sucesivamente. La lista con los 10
primeros números sería esta: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34].
Queremos hacer un programa que reciba un número por teclado y nos calcule tantos
números de la sucesión de fibonacci como indique ese número. Por ejemplo, si
metemos un 8 la salida de tu programa debería de ser así:
0,1,1,2,3,5,8,13"""

def calcularSucesionDeFibonacci(numero):
    if numero <= 0:
        return ""

    if numero == 1:
        return "0"

    if numero == 2:
        return "0,1"

    a = 0
    b = 1
    cadena = "0,1"

    for i in range(numero - 2):
        c = a + b
        cadena += f",{c}"
        a = b
        b = c

    return cadena


numero = int(input("Introduce un número: "))
print(calcularSucesionDeFibonacci(numero))


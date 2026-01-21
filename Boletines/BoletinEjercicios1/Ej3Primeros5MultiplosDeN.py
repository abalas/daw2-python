def enseniarMenu():
    print("1. Devolver primeros 5 múltiplos de un número", "2. Salir del programa", sep="\n")

def devolverPrimeros5Multiplos(num):
    for i in range(1, 6):
        print(num * i)

def saliendo():
    print("Saliendo...")

while 2==2:
    enseniarMenu()
    opcion = int(input("Seleccione una de las opciones: "))
    if opcion == 1:
        numero = int(input("Ingrese un número: "))
        devolverPrimeros5Multiplos(numero)
    elif opcion == 2:
        saliendo()
        break
    else:
        print("Opción inválida")
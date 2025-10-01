
numero= 9

bandera  = True

while bandera:
    numero = int(input("Introduzca un numero: "))
    match numero:
        case 2:
            print("El número es el 2")
            bandera = False
        case 3 | 4:
            print("El número es el 3 o el 4")
            bandera = False
        case _:
            print("Opcion por invalida, prueba con 2,3 o 4")


    print("FIN")

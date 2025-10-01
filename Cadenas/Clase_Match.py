
numero= 9

bandera  = False

while bandera==False:
    numero = int(input("P o J para jugar, C para configurar, X para salir "))
    match numero:
        case "P" | "p" | "J" | "j":
            print("El número es el 2")
        case "C":
            print("El número es el 3 o el 4")
        case "X":
            badera = False
        case _:
            print("Opcion por invalida, prueba con 2,3 o 4")


    print("FIN")

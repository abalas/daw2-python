
inputValido= False
while inputValido==False:
    try:
        numero = int(input("Introduce un número: "))
        resultado = 10/numero
        print(resultado)
    except ZeroDivisionError:
        print("no se pude dividir por 0")
    except ValueError:
        print("No has metido un entorno")
    except:
        print("Excepcion, pero otra")
    else:
        print("No ha ocurrido ninguna excepcion")
        inputValido = True
    finally:
        print("Seguimos adelante...")
    print("Programa finalizado")

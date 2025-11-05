salir = False
while salir == False:
    try:
        numero = int( int("Introduce un numero positivo y entero"))
        resultado = 10/numero
        if numero < 0:
            raise ZeroDivisionError("No es un numero positivo")
    except ZeroDivisionError:
        print("no se puede dividir con negativos")
    except ValueError:
        print("No es un entero")
    except:
        print("Excepcion pero otra")
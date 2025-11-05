salir = False
while not salir:
    try:
        numero = int(input("Introduce un número positivo y entero: "))
        assert numero >= 0, "No admito números negativos"
        resultado = 10 / numero
        print(f"Resultado: {resultado}")
        salir = True
    except AssertionError as e:
        print(e)
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    except ValueError:
        print("No es un número entero válido")
    except Exception as e:
        print(f"Otra excepción: {e}")

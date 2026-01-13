

numero = input("Introduzca un número: ")
if numero.isdigit():
    print(f"""El numero de digitos que tiene el numero es: {len(numero)}""")
else:
    print("Ha introducido un formato no valido")
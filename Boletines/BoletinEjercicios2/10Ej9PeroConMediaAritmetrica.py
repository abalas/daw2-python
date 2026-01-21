finalizado = False
cont_entradas_validas = 0
cont_entradas_invalidas = 0

minimo = None
maximo = None

while not finalizado:
    entrada = input("Introduzca un número del 1 al 100 o FIN para terminar: ")

    if entrada == "FIN":
        finalizado = True
    else:
        # Validación de número
        if entrada.isdigit():  # Verifica que son solo dígitos
            numero = int(entrada)
            if 1 <= numero <= 100:
                cont_entradas_validas += 1

                # Actualizar mínimo y máximo
                if minimo is None or numero < minimo:
                    minimo = numero
                if maximo is None or numero > maximo:
                    maximo = numero

            else:
                cont_entradas_invalidas += 1
                print("Error: el número debe estar entre 1 y 100.")
        else:
            cont_entradas_invalidas += 1
            print("Error: entrada inválida. Debe ser un número o FIN.")

print(f"\nNúmero de entradas válidas: {cont_entradas_validas}")
print(f"Número de entradas inválidas: {cont_entradas_invalidas}")
print(f"Entradas totales: {cont_entradas_validas + cont_entradas_invalidas}")

# Mostrar mínimo y máximo si hubo entradas válidas
if cont_entradas_validas > 0:
    print(f"Número mínimo introducido: {minimo}")
    print(f"Número máximo introducido: {maximo}")
else:
    print("No se introdujeron números válidos.")

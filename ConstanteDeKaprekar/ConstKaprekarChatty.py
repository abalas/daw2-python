def calculoConstKepler(numero):
    """Calcula un paso del proceso de Kaprekar para un número de 4 cifras."""

    # Convertimos el número en cadena con 4 dígitos (por si pierde ceros a la izquierda)
    numero = f"{int(numero):04d}"

    # Ordenamos los dígitos en orden ascendente y descendente
    nAscendente = ''.join(sorted(numero))
    nDescendente = ''.join(sorted(numero, reverse=True))

    # Calculamos la diferencia
    resultado = int(nDescendente) - int(nAscendente)

    # Mostramos la operación con formato de 4 dígitos
    print(f"{nDescendente} - {nAscendente} = {resultado:04d}")

    return resultado


# -------------------------------
# Validación de entrada del usuario
# -------------------------------
while True:
    numero = input("Introduce un número de 4 cifras con cada dígito distinto entre sí: ")

    if not numero.isdigit() or len(numero) != 4:
        print("❌ Debe tener exactamente 4 dígitos numéricos.")
        continue

    if len(set(numero)) != 4:
        print("❌ Los dígitos deben ser distintos entre sí.")
        continue

    if len(set(numero)) == 1:
        print("❌ No puede tener los 4 dígitos iguales.")
        continue

    # Si pasa todas las comprobaciones, salimos del bucle
    break

# -------------------------------
# Proceso iterativo hasta llegar a la constante de Kaprekar (6174)
# -------------------------------
contador = 0
resultado = int(numero)

print("\n--- Proceso de Kaprekar ---")

while resultado != 6174:
    resultado = calculoConstKepler(resultado)
    contador += 1

print(f"\n✅ Se ha alcanzado la constante de Kaprekar (6174) en {contador} iteraciones.")

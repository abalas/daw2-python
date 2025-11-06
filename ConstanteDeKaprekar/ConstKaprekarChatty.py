def calculoConstKepler(numero):
    # Convertimos el número en lista de dígitos
    nAscendente = ''.join(sorted(numero))
    nDescendente = ''.join(sorted(numero, reverse=True))

    resultado = int(nDescendente) - int(nAscendente)
    print(f"{nDescendente} - {nAscendente} = {resultado:04d}")
    return resultado


# Validación de entrada
numero_valido = False

while not numero_valido:
    numero = input("Introduce un número de 4 cifras con cada dígito distinto entre sí: ")

    if len(numero) != 4 or not numero.isdigit():
        print("❌ Debe tener exactamente 4 dígitos numéricos.")
        continue

    if len(set(numero)) != 4:
        print("❌ Los dígitos deben ser distintos entre sí.")
        continue

    numero_valido = True

# Proceso iterativo hasta llegar a la constante de Kaprekar (6174)
contador = 1
resultado = calculoConstKepler(numero)

while resultado != 6174:
    numero = f"{resultado:04d}"  # Aseguramos que siempre tenga 4 cifras
    resultado = calculoConstKepler(numero)
    contador += 1

print(f"\n✅ Se ha alcanzado la constante de Kaprekar (6174) en {contador} iteraciones.")

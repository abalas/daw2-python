import aleatorio

def esta(x, lista):
    return x in lista

maximo = int(input("Introduce un número: "))

# Lista de pares posibles
pares_disponibles = [n for n in range(2, maximo+1, 2)]

if len(pares_disponibles) < 5:
    print("No hay suficientes números pares para generar 5 distintos.")
else:
    numsAle = []
    while len(numsAle) < 5:
        x = random.choice(pares_disponibles)
        if not esta(x, numsAle):
            numsAle.append(x)

    print(f"5 números pares aleatorios y diferentes comprendidos entre 1 y {maximo}:")
    print(*numsAle, sep=", ")

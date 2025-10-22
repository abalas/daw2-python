# Ejercicio 2: Generar 10 números aleatorios, contar pares e impares, mayor y menor
import aleatorio

print("10 números entre el 1 y el 1000")

numeros = [random.randint(1, 1000) for _ in range(10)]

# Mostrar los números separados por coma y espacio
print(' , '.join(map(str, numeros)))

# Contar pares e impares
pares = sum(1 for n in numeros if n % 2 == 0)
impares = len(numeros) - pares

# Encontrar mayor y menor
mayor = max(numeros)
menor = min(numeros)

print(f"He generado {pares} números pares y {impares} impares")
print(f"El número mayor ha sido el {mayor} y el menor el {menor}")

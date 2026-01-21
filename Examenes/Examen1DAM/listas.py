# Referencia completa de listas en Python
# Archivo de guía para estudios y exámenes

# 1. Crear listas
lista1 = [1, 2, 3, 4]
lista2 = ['a', 'b', 'c']
lista_vacia = []

# 2. Acceso a elementos (indexing)
primer_elemento = lista1[0]
ulimo_elemento = lista1[-1]
print(primer_elemento, ulimo_elemento)

# 3. Slicing (sublistas)
sublista = lista1[1:3]  # elementos 1 y 2
sublista2 = lista1[:2]  # primeros dos elementos
sublista3 = lista1[2:]  # desde índice 2 hasta el final
print(sublista, sublista2, sublista3)

# 4. Modificación de elementos
lista1[0] = 10
print(lista1)

# 5. Añadir elementos
lista1.append(5)           # agrega al final
lista1.insert(1, 15)       # inserta en índice 1
print(lista1)

# 6. Extender lista
lista1.extend([6,7,8])     # agrega múltiples elementos
print(lista1)

# 7. Eliminar elementos
lista1.remove(15)           # elimina primer elemento con valor 15
ultimo = lista1.pop()       # elimina y devuelve último elemento
indice2 = lista1.pop(1)     # elimina y devuelve elemento índice 1
print(lista1, ultimo, indice2)

# 8. Ordenar y revertir
lista_numeros = [4, 1, 9, 3]
lista_numeros.sort()       # orden ascendente
print("sorted:", lista_numeros)
lista_numeros.sort(reverse=True) # descendente
print("reverse sort:", lista_numeros)
lista_numeros.reverse()    # invierte el orden
print("reversed:", lista_numeros)

# 9. Buscar elementos
posicion = lista2.index('b')  # devuelve índice de primer 'b'
existe = 'c' in lista2         # True/False
print(posicion, existe)

# 10. Contar elementos
cuenta = lista2.count('b')      # cuántas veces aparece 'b'
print(cuenta)

# 11. Copiar listas
copia = lista1.copy()           # copia superficial
copia2 = lista1[:]              # otra forma de copiar
print(copia, copia2)

# 12. Limpiar lista
lista2.clear()                  # elimina todos los elementos
print(lista2)

# 13. Longitud
lon = len(lista1)
print("Longitud:", lon)

# 14. Concatenar y repetir listas
lista_concat = lista1 + [20, 30]
lista_repetir = lista1 * 2
print(lista_concat, lista_repetir)

# 15. Iterar sobre listas
for elem in lista1:
    print(elem, end=' ')
print()

# 16. Listas anidadas
matriz = [[1,2,3],[4,5,6]]
elem = matriz[1][2]  # 6
print(elem)

# 17. Comprensión de listas
cuadrados = [x**2 for x in range(5)]
pares = [x for x in range(10) if x%2==0]
print(cuadrados, pares)

# 18. Funciones útiles con listas
suma = sum([1,2,3])
maximo = max([1,2,3])
minimo = min([1,2,3])
print(suma, maximo, minimo)

# 19. Copiar listas profundas (para listas anidadas)
import copy
lista_anidada = [[1,2],[3,4]]
copia_profunda = copy.deepcopy(lista_anidada)
print(copia_profunda)

# Fin de referencia completa de listas en Python

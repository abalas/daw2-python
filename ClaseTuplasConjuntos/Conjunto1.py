conjunto1 = {"Ana", "Pedro", "Luis", "Eva"}
conjunto2 = set(["Ana", "Pedro", "Luis", "Eva"])
print(conjunto1)
print(conjunto2)
print(conjunto1[0])

if "Ana" in conjunto1:
    print("Ana está")
    print(conjunto1)
conjunto1.add("Manuel")
conjunto1.add("Manuel")
print(conjunto1.remove("Ana"))     # cuando queramos saber si existe o no exte el elemento a borrar
print(conjunto1)
conjunto1.discard("Eustaquio")  # no da error si no existe
print(conjunto1.pop())   # extrae al "azar" y elimina
print(conjunto1)
conjunto1.clear()
print(conjunto1)

# resumen_conjuntos.py
# ======================================================
# 🧩 CONJUNTOS (set) EN PYTHON
# ======================================================

# Un CONJUNTO (set) es una colección DESORDENADA y SIN ELEMENTOS REPETIDOS.
# Se usa para almacenar elementos únicos, y permite realizar operaciones
# matemáticas como unión, intersección y diferencia.

# ------------------------------------------------------
# 🟢 CREACIÓN DE CONJUNTOS
# ------------------------------------------------------

# Literalmente con llaves
conjunto1 = {"Ana", "Pedro", "Luis", "Eva"}

# A partir de una lista (con la función set)
conjunto2 = set(["Pedro", "Ana", "Laura", "Luis"])

# Conjunto vacío (IMPORTANTE: {} crea un diccionario, no un set)
conjunto_vacio = set()

# ------------------------------------------------------
# 🔵 PROPIEDADES IMPORTANTES
# ------------------------------------------------------
# - No tienen orden → el orden puede variar al imprimir.
# - No permiten duplicados.
# - Son mutables (puedes agregar o quitar elementos).
# - Sus elementos deben ser inmutables (números, cadenas, tuplas...).

# ------------------------------------------------------
# 🟣 OPERACIONES BÁSICAS
# ------------------------------------------------------

# Agregar elementos
conjunto1.add("Sofía")

# Eliminar elementos
conjunto1.remove("Ana")      # Si no existe, lanza error
conjunto1.discard("Pepe")    # Si no existe, no lanza error

# Eliminar un elemento aleatorio
conjunto1.pop()

# Vaciar el conjunto
# conjunto1.clear()

print("Conjunto 1:", conjunto1)

# ------------------------------------------------------
# 🟠 OPERACIONES ENTRE CONJUNTOS
# ------------------------------------------------------

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Unión (elementos de ambos)
print("Unión:", A | B)
print("Unión (método):", A.union(B))

# Intersección (elementos comunes)
print("Intersección:", A & B)
print("Intersección (método):", A.intersection(B))

# Diferencia (elementos que están en A pero no en B)
print("Diferencia:", A - B)
print("Diferencia (método):", A.difference(B))

# Diferencia simétrica (elementos que están en uno u otro, pero no en ambos)
print("Diferencia simétrica:", A ^ B)
print("Diferencia simétrica (método):", A.symmetric_difference(B))

# ------------------------------------------------------
# 🟡 MÉTODOS ÚTILES
# ------------------------------------------------------
C = {10, 20, 30}
D = {20, 30}

print("¿D está contenido en C?", D.issubset(C))         # Subconjunto
print("¿C contiene a D?", C.issuperset(D))              # Superconjunto
print("¿C y A son disjuntos?", C.isdisjoint(A))         # Sin elementos comunes

# ------------------------------------------------------
# 🔴 DIFERENCIAS CON LISTAS
# ------------------------------------------------------
# - Los conjuntos no tienen orden → no se puede acceder por índice (ej: conjunto[0] ❌)
# - No permiten elementos repetidos.
# - Son más rápidos para búsquedas ("in").

print("¿3 está en A?", 3 in A)   # True

# ------------------------------------------------------
# 🧠 RESUMEN FINAL
# ------------------------------------------------------
# ✔️ set() → colección sin duplicados
# ✔️ No tiene orden
# ✔️ Ideal para comparar y eliminar duplicados
# ✔️ Soporta operaciones de teoría de conjuntos

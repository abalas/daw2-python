"""
============================================================
               🔥 CHULETA DEFINITIVA DEL FOR EN PYTHON 🔥
============================================================

📌 1. SINTAXIS BÁSICA
------------------------------------------------------------
for variable in iterable:
    # código a ejecutar

- ITERABLE = lista, string, tupla, rango, diccionario, set, generador…

Ejemplo:
for x in [1, 2, 3]:
    print(x)


📌 2. USO DE RANGE()
------------------------------------------------------------
range(fin)                 → 0..fin-1
range(inicio, fin)         → inicio..fin-1
range(inicio, fin, paso)   → con paso

Ejemplos:
for i in range(5):                # 0,1,2,3,4
for i in range(2, 10):            # 2..9
for i in range(10, 0, -1):        # cuenta atrás
for i in range(0, 20, 2):         # pares


📌 3. RECORRER AL REVÉS
------------------------------------------------------------
lista[::-1]
reversed(lista)
range(inicio, fin, -paso)

Ejemplos:
for x in lista[::-1]:
for x in reversed(lista):
for i in range(10, -1, -1):


📌 4. RECORRER STRINGS
------------------------------------------------------------
for letra in "Python":
    print(letra)

- También funciona con emojis y caracteres especiales.


📌 5. RECORRER TUPLAS Y SETS
------------------------------------------------------------
for x in (1, 2, 3):
for x in {1, 2, 3}:
# OJO → los sets NO mantienen orden


📌 6. RECORRER DICCIONARIOS
------------------------------------------------------------
dicc.keys()        → claves
dicc.values()      → valores
dicc.items()       → clave + valor

Ejemplos:
for k in dicc:
for v in dicc.values():
for k, v in dicc.items():


📌 7. OBTENER ÍNDICE + VALOR (enumerate)
------------------------------------------------------------
for i, valor in enumerate(lista):
    print(i, valor)

Opciones:
enumerate(lista, start=1)


📌 8. BUCLES ANIDADOS
------------------------------------------------------------
for i in range(3):
    for j in range(2):
        print(i, j)


📌 9. LIST COMPREHENSIONS (versión compacta del for)
------------------------------------------------------------
nueva_lista = [x * 2 for x in lista]
filtrada = [x for x in lista if x > 10]

Con condicional ELSE:
["par" if x % 2 == 0 else "impar" for x in numeros]


📌 10. DICT COMPREHENSIONS
------------------------------------------------------------
cuadrados = {x: x*x for x in range(10)}


📌 11. SET COMPREHENSIONS
------------------------------------------------------------
pares = {x for x in range(20) if x % 2 == 0}


📌 12. FOR CON BREAK Y CONTINUE
------------------------------------------------------------
break → corta el bucle
continue → salta a la siguiente iteración

Ejemplos:
for x in numeros:
    if x < 0:
        break

for x in numeros:
    if x == 0:
        continue


📌 13. FOR + ELSE (MUY POCO CONOCIDO)
------------------------------------------------------------
El bloque ELSE se ejecuta si el bucle termina sin break.

for n in numeros:
    if n < 0:
        break
else:
    print("No había números negativos")


📌 14. ITERAR VARIAS LISTAS A LA VEZ (zip)
------------------------------------------------------------
nombres = ["Ana", "Luis", "Sara"]
edades = [20, 30, 25]

for nombre, edad in zip(nombres, edades):
    print(nombre, edad)


📌 15. DESENPAQUETADO AUTOMÁTICO EN EL FOR
------------------------------------------------------------
pares = [(1,2), (3,4), (5,6)]

for a, b in pares:
    print(a, b)

También sirve con tuplas de 3, 4 o más elementos.


📌 16. FOR CON GENERADORES (eficientes)
------------------------------------------------------------
for x in (n*n for n in range(1000000)):
    print(x)


📌 17. ITERAR SOBRE LÍNEAS DE UN ARCHIVO
------------------------------------------------------------
with open("archivo.txt") as f:
    for linea in f:
        print(linea)


📌 18. ERRORES COMUNES
------------------------------------------------------------
❌ for i in 10:                 # NO es iterable
❌ for i in range(10, 0):       # NO cuenta hacia atrás sin paso
❌ modificar lista mientras se itera → usar copia: lista[:]


📌 19. CONSEJOS PRO
------------------------------------------------------------
✔ Usar enumerate() en vez de range(len()).
✔ Usar zip() para listas paralelas.
✔ Usar comprehensions cuando sea simple.
✔ Evitar bucles muy pesados → usar generadores.

============================================================
"""

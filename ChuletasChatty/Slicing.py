"""
=====================================================================
          🐍🔥 ULTRA CHULETA COMPLETA DEL SLICING EN PYTHON 🔥🐍
=====================================================================

El SLICING es una técnica para obtener partes de secuencias en Python:
- strings
- listas
- tuplas
- range (solo convertirlo a lista)
- bytes, bytearray
- NO funciona con SETS (no tienen orden)

La sintaxis general es:

    secuencia[inicio:fin:paso]

---------------------------------------------------------------------
 1) SIGNIFICADO DE CADA PARTE
---------------------------------------------------------------------
inicio → índice donde empieza el corte (incluido)
fin    → índice donde termina (EXCLUIDO)
paso   → salto entre elementos (por defecto 1)

Ejemplo:
texto[2:7]
Toma desde índice 2 hasta el 6.

---------------------------------------------------------------------
 2) SLICING BÁSICO
---------------------------------------------------------------------
lista = [0,1,2,3,4,5,6]

lista[2:5]    → [2,3,4]
lista[:4]     → [0,1,2,3]      # inicio omitido ⇒ desde 0
lista[3:]     → [3,4,5,6]      # fin omitido ⇒ hasta el final
lista[:]      → copia completa

---------------------------------------------------------------------
 3) SLICING CON PASO
---------------------------------------------------------------------
lista[::2]    → elementos de 2 en 2
lista[1:6:2]  → desde 1 hasta 5 saltando de 2

Ejemplos:
lista = [0,1,2,3,4,5,6]

lista[::2]   → [0,2,4,6]
lista[1::2]  → [1,3,5]

---------------------------------------------------------------------
 4) SLICING CON ÍNDICES NEGATIVOS
---------------------------------------------------------------------
Índices negativos cuentan desde el final:

-1 → último
-2 → penúltimo
etc.

Ejemplos:
texto = "Python"

texto[-3:]   → "hon"
texto[:-3]   → "Pyt"
texto[-5:-1] → "ytho"

---------------------------------------------------------------------
 5) INVERTIR UNA SECUENCIA CON SLICING
---------------------------------------------------------------------
texto[::-1]
lista[::-1]

Ejemplos:
"Python"[::-1] → "nohtyP"
[1,2,3][::-1]  → [3,2,1]

Es la forma más rápida y "pythonica" de invertir.

---------------------------------------------------------------------
 6) COPIAR UNA LISTA / STRING
---------------------------------------------------------------------
lista2 = lista[:]  # copia superficial (shallow copy)

También funciona con strings:

copia = texto[:]

---------------------------------------------------------------------
 7) SLICING SIN ROMPER EL PROGRAMA (Límites fuera de rango)
---------------------------------------------------------------------
Python NO lanza error si te pasas:

texto = "Hola"

texto[0:100]   → "Hola"
texto[-100:2]  → "Ho"

Esto lo hace mucho más seguro que manipular índices manualmente.

---------------------------------------------------------------------
 8) USAR SOLO EL PASO (omitir inicio y fin)
---------------------------------------------------------------------
lista[::1]  → copia exacta
lista[::-1] → invertida
lista[::3]  → cada 3 elementos

---------------------------------------------------------------------
 9) SLICING EN STRINGS
---------------------------------------------------------------------
texto = "Python"

texto[1:4]   → "yth"
texto[::2]   → "Pto"
texto[::-1]  → "nohtyP"

---------------------------------------------------------------------
10) SLICING EN TUPLAS
---------------------------------------------------------------------
tupla = (10, 20, 30, 40)

tupla[:2]   → (10, 20)
tupla[::-1] → (40, 30, 20, 10)

---------------------------------------------------------------------
11) SLICING EN LISTAS
---------------------------------------------------------------------
Muy usado para editar partes:

lista = [1,2,3,4,5]

lista[1:3] = [20,30,40]
→ [1, 20, 30, 40, 4, 5]

Borrar elementos:
del lista[2:4]

Insertar:
lista[2:2] = [100,200]

---------------------------------------------------------------------
12) SLICING EN OBJETOS MULTIDIMENSIONALES
---------------------------------------------------------------------
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matriz[0]        → [1,2,3]
matriz[0][1:]    → [2,3]
[ fila[1:] for fila in matriz ]   → cortar columnas

No existe slicing de 2D tipo matriz[:,:] a menos que uses NumPy.

---------------------------------------------------------------------
13) SLICING CON EL OBJETO slice()
---------------------------------------------------------------------
También se puede crear un slice reutilizable:

s = slice(1, 5, 2)

lista[s]

Ejemplo:
lista = [10,20,30,40,50,60]
lista[s] → [20,40]

---------------------------------------------------------------------
14) SLICING SOBRE RANGES (solo tras convertir)
---------------------------------------------------------------------
range no soporta slicing directo:

range(10)[2:7] → ERROR

Debes convertirlo:
list(range(10))[2:7]

---------------------------------------------------------------------
15) ERRORES COMUNES
---------------------------------------------------------------------
❌ lista[1,4]   # coma NO funciona
✔ lista[1:4]

❌ lista[1:4:0] # paso 0 no válido
✔ paso debe ser distinto de cero

❌ usar set con slicing
✔ sets NO admiten slicing porque no tienen orden

---------------------------------------------------------------------
16) TRUCOS Y PATRONES TÍPICOS DE SLICING
---------------------------------------------------------------------
👉 Obtener los 3 primeros
lista[:3]

👉 Obtener los 3 últimos
lista[-3:]

👉 Eliminar el primer elemento
lista[1:]

👉 Eliminar el último
lista[:-1]

👉 Tomar elementos en posición par
lista[::2]

👉 Tomar elementos en posición impar
lista[1::2]

👉 Recorrer al revés saltando de 2 en 2
lista[::-2]

👉 Comprobar palíndromos
palabra == palabra[::-1]

👉 Quedarse con todo menos el primero y el último
lista[1:-1]

👉 Cortar string sin fallar aunque esté vacío
texto[:1000]

---------------------------------------------------------------------
17) COMBINAR SLICING + JOIN (strings avanzados)
---------------------------------------------------------------------
Invertir palabras:
" ".join(palabra[::-1] for palabra in texto.split())

Ejemplo:
"Hola Mundo" → "aloH odnuM"

---------------------------------------------------------------------
18) SLICING PARA LIMPIAR DATOS
---------------------------------------------------------------------
Eliminar caracteres:

texto = texto.strip()      # bordes
texto = texto[1:-1]        # quitar el primero y el último
texto = texto.replace(" ", "")

---------------------------------------------------------------------
19) SLICING COMO ALTERNATIVA A BUCLES
---------------------------------------------------------------------
lista[::2] es más rápido y más pythonico que:

for i in range(0, len(lista), 2):
    print(lista[i])

---------------------------------------------------------------------
20) SLICING PARA CREAR SUBSECUENCIAS GRANDES
---------------------------------------------------------------------
Muy eficiente porque NO copia realmente toda la secuencia,
solo genera una vista (en Python CPython las listas sí copian,
pero strings/tuplas no).

---------------------------------------------------------------------

====================== FIN DE LA SUPER CHULETA ======================
"""

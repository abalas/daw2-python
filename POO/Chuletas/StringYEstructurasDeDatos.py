# =========================================================
# CHULETA COMPLETÍSIMA: STRINGS Y ESTRUCTURAS DE DATOS EN PYTHON
# Archivo de referencia (.py)
# =========================================================

# ---------------------------------------------------------
# 1. STRINGS (CADENAS)
# ---------------------------------------------------------

texto = "Hola Mundo"

# Longitud
print(len(texto))

# Acceso por índice
print(texto[0])  # 'H'
print(texto[-1]) # 'o'

# Slicing
print(texto[0:4])  # 'Hola'
print(texto[5:])   # 'Mundo'
print(texto[:4])    # 'Hola'

# Métodos importantes
print(texto.lower())   # 'hola mundo'
print(texto.upper())   # 'HOLA MUNDO'
print(texto.capitalize()) # 'Hola mundo'
print(texto.strip())   # Elimina espacios al inicio/final
print(texto.replace('Mundo', 'Python'))
print(texto.split())   # ['Hola','Mundo']
print(' '.join(['Hola','Python']))
print(texto.startswith('Ho'))  # True
print(texto.endswith('do'))    # True
print(texto.find('Mundo'))     # 5 (posición)
print(texto.count('o'))        # 2

# Formateo
nombre = 'Ana'
edad = 25
print(f'{nombre} tiene {edad} años')  # f-string
print('{} tiene {} años'.format(nombre, edad))
print('%s tiene %d años' % (nombre, edad))


# ---------------------------------------------------------
# 2. LISTAS
# ---------------------------------------------------------

lista = [1,2,3,4,5]
lista2 = ['a','b','c']

# Acceso
print(lista[0])
print(lista[-1])
print(lista[1:3])

# Métodos
lista.append(6)
lista.insert(0,0)
lista.remove(3)
lista.pop()
lista.sort()
lista.reverse()

# Comprehension
cuadrados = [x**2 for x in lista]
pares = [x for x in lista if x%2==0]


# ---------------------------------------------------------
# 3. TUPLAS
# ---------------------------------------------------------

tupla = (1,2,3,4)
# Inmutable, indexado, soporta slicing
# Métodos: count, index


# ---------------------------------------------------------
# 4. CONJUNTOS (SETS)
# ---------------------------------------------------------

conjunto = {1,2,3,4,4}  # {1,2,3,4}
conjunto.add(5)
conjunto.remove(2)
conjunto.discard(10)   # no lanza error si no existe

# Operaciones
a = {1,2,3}
b = {2,3,4}
print(a.union(b))       # {1,2,3,4}
print(a.intersection(b))# {2,3}
print(a.difference(b))  # {1}
print(a.symmetric_difference(b)) # {1,4}

# Comprehension de sets
set_cuadrados = {x**2 for x in range(5)}


# ---------------------------------------------------------
# 5. DICCIONARIOS
# ---------------------------------------------------------

dic = {'nombre':'Ana','edad':25}
print(dic['nombre'])
print(dic.get('edad'))
print(dic.get('altura','No definida'))

# Añadir / modificar
dic['ciudad'] = 'Madrid'
dic['edad'] = 26

# Eliminar
dic.pop('ciudad')
del dic['edad']

# Recorrer
for k,v in dic.items():
    print(k,v)

for k in dic.keys():
    print(k)

for v in dic.values():
    print(v)

# Comprensión
dic2 = {x:x**2 for x in range(5)}


# ---------------------------------------------------------
# 6. CONVERSIONES ENTRE ESTRUCTURAS
# ---------------------------------------------------------

lista = [1,2,3]
tupla = tuple(lista)
set1 = set(lista)
dic = {i:i*2 for i in lista}


# ---------------------------------------------------------
# 7. ESTRUCTURAS ANIDADAS
# ---------------------------------------------------------

matriz = [[1,2],[3,4],[5,6]]
print(matriz[1][0])  # 3

personas = [{'nombre':'Ana','edad':25},{'nombre':'Luis','edad':30}]
print(personas[0]['nombre'])  # 'Ana'


# ---------------------------------------------------------
# 8. ITERAR ESTRUCTURAS
# ---------------------------------------------------------

for i, valor in enumerate(lista):
    print(i, valor)

for fila in matriz:
    for elemento in fila:
        print(elemento)

for clave, valor in dic.items():
    print(clave, valor)


# ---------------------------------------------------------
# 9. TRUCOS Y ERRORES TÍPICOS
# ---------------------------------------------------------
# ❌ Confundir tupla y lista (mutabilidad)
# ❌ Acceder a diccionario con key inexistente sin get
# ❌ Sumar sets con + ❌ (usar union)
# ❌ Modificar lista mientras iteras
# ❌ Olvidar keys() o values() en bucles

# =========================================================
# FIN DE LA CHULETA DE STRINGS Y ESTRUCTURAS DE DATOS
# =========================================================

"""Las tuplas son listas de valores constantes"""
lista = [1,2,3]
tupla = (1,2,3)
tupla2 =("Ana","Pepe", "Pedro")
tupla3 = ("María", 28.5, False)
tupla4 = 4,5,6
print(tupla)
print(tupla4)
tupla5=()     #no se pude
pi=(3.14159)  #no se puede
pi2=(3.14159,) # asi si
tupla6 = tuple(lista)
lista2 = list(tupla4)
print(lista2)
texto = str(tupla6)
print(texto)
tupla7 = (1,2,(1,3,4),5,[1,2,3],7)
print(tupla7)
print(tupla7[1])
print(tupla7[4])
print(tupla7[-2])
tupla7[4][0] = 33
print(tupla7[4])
print(tupla7)


# tupla_python_intro.py

# 1️⃣ Crear tuplas
numeros = (1, 2, 3, 4, 5)
persona = ("Ana", 28, "Madrid")
solo_uno = (42,)  # Tupla de un solo elemento

# 2️⃣ Acceder a elementos
print("Acceder a elementos de la tupla persona:")
print(persona[0])  # Ana
print(persona[1])  # 28
print(persona[-1])  # Madrid

# 3️⃣ Recorrer tupla
print("\nRecorrer tupla persona:")
for dato in persona:
    print(dato)

# 4️⃣ Operaciones con tuplas
# Concatenar tuplas
tupla1 = (1, 2)
tupla2 = (3, 4)
tupla3 = tupla1 + tupla2
print("\nConcatenar tuplas:", tupla3)

# Repetir tuplas
print("Repetir tupla (0,1) * 3:", (0, 1) * 3)

# Verificar existencia de elemento
print("¿2 está en tupla3?", 2 in tupla3)

# 5️⃣ Ejemplo práctico: coordenadas
coordenadas = ((0,0), (1,2), (3,4))
print("\nCoordenadas:")
for x, y in coordenadas:
    print(f"x={x}, y={y}")

# 6️⃣ Fundamentos (comentarios)
# Las tuplas son inmutables, ordenadas, heterogéneas y pueden ser usadas como claves en diccionarios.


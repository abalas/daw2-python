"""
===============================================================
    CHULETA COMPLETA DE str.maketrans() Y str.translate()
===============================================================

Estas dos funciones sirven para SUSTITUIR O ELIMINAR caracteres
de forma rápida, eficiente y elegante en Python.

translate = aplica una tabla de traducción a una cadena
maketrans = crea la tabla de traducción

Son perfectas para:
- transformar texto
- cifrados básicos (leet, ROT13, etc.)
- eliminar caracteres (puntuación, espacios, acentos…)
- normalizar cadenas grandes muy rápido (implementado en C)

===============================================================
1) str.maketrans(s1, s2)
---------------------------------------------------------------
Crea una tabla de traducción emparejando posiciones:
cada carácter de s1 → carácter en misma posición de s2

REQUISITO: ambas cadenas deben tener la MISMA LONGITUD.

Ejemplo:
"""

tabla = str.maketrans("abc", "123")
print("abcxyz".translate(tabla))
# SALIDA: 123xyz
# 'a'→'1', 'b'→'2', 'c'→'3'

"""
===============================================================
2) str.maketrans(s1, s2, s3)
---------------------------------------------------------------
Además de sustituir, permite BORRAR caracteres.

Los caracteres de s3 se ELIMINAN del texto.

Ejemplo:
"""

tabla = str.maketrans("ae", "43", " !?")
print("¿Qué hace esto?".translate(tabla))
# SALIDA: Qu3h4c3est0
# a→4, e→3 y los caracteres de " !?" se eliminan

"""
===============================================================
3) str.maketrans(diccionario)
---------------------------------------------------------------
La forma más flexible.
El diccionario debe mapear:
- caracteres → cadenas
- o ord(caracter) → cadenas
- o ord(caracter) → None (eliminar)

Ejemplo:
"""

tabla = str.maketrans({
    "ñ": "n",
    "á": "a",
    "é": "e",
    ord("!"): None,   # eliminar
})
print("Información!".translate(tabla))
# SALIDA: Informacion

"""
===============================================================
4) ¿QUÉ HACE EXACTAMENTE translate(tabla)?
---------------------------------------------------------------
translate recorre cada carácter de la cadena:
1. Obtiene su ord() → código Unicode
2. Busca ese código en la tabla:
   - Si está mapeado a una CADENA → lo reemplaza
   - Si está mapeado a un ENTERO → usa ese código Unicode
   - Si está mapeado a None → lo ELIMINA
   - Si no está → lo deja igual

¡¡SÚPER RÁPIDO!! Ideal para grandes textos.

===============================================================
5) EJEMPLOS PRÁCTICOS Y ÚTILES
===============================================================
"""

# EJEMPLO 1: Texto estilo hacker (LEET)
tabla = str.maketrans("aeioAEIO", "43104310")
print("Hola MUNDO".translate(tabla))
# SALIDA: H0l4 MUND0


# EJEMPLO 2: Eliminar puntuación
import string
tabla = str.maketrans("", "", string.punctuation)
print("¡Hola, mundo! ¿Cómo estás?".translate(tabla))
# SALIDA: Hola mundo Cómo estás


# EJEMPLO 3: Quitar espacios y saltos de línea
tabla = str.maketrans("", "", " \n\t")
print("Hola   mundo\notro\tejemplo".translate(tabla))
# SALIDA: Holamundootroejemplo


# EJEMPLO 4: Cambiar vocales por 'x' (misma longitud)
tabla = str.maketrans("aeiouAEIOU", "xxxxxxxxxx")
print("Programación".translate(tabla))
# SALIDA: Prxgrxmxcxxn


# EJEMPLO 5: Sustituir varios caracteres por una cadena más larga
tabla = str.maketrans({
    "&": " AND ",
    "@": " (ARROBA) ",
})
print("correo@mail.com & telefono".translate(tabla))
# SALIDA: correo (ARROBA) mail.com  AND  telefono


# EJEMPLO 6: Normalizar tildes a su versión sin acento
tabla = str.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU")
print("Información Útil".translate(tabla))
# SALIDA: Informacion Util


"""
===============================================================
6) PATRÓN TÍPICO RECOMENDADO
---------------------------------------------------------------
Si necesitas muchas sustituciones:
- Usa maketrans con diccionario
- translate para aplicar
===============================================================
"""

tabla = str.maketrans({
    "a": "4", "A": "4",
    "e": "3", "E": "3",
    "i": "1", "I": "1",
    "o": "0", "O": "0",
})
print("Aprendiendo Python".translate(tabla))
# SALIDA: 4pr3nd13nd0 Pyth0n

"""
===============================================================
7) NOTAS IMPORTANTES
---------------------------------------------------------------
✔ translate es más rápido que usar .replace() muchas veces  
✔ maketrans puede ELIMINAR caracteres (replace NO)  
✔ translate NO modifica la cadena original (las cadenas son inmutables)  
✔ La tabla internamente usa códigos Unicode (enteros)  
✔ Ideal para procesar archivos grandes o textos extensos  
===============================================================
FIN DE LA CHULETA
===============================================================
"""

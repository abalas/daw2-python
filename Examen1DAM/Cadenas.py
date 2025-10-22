# Referencia completa de funciones y métodos de cadenas en Python
# Este archivo sirve para tenerlo como guía durante estudios y exámenes

# 1. Crear cadenas
cadena1 = 'Hola'
cadena2 = "Mundo"
cadena3 = '''Cadena multilínea'''

# 2. Concatenación
concat = cadena1 + ' ' + cadena2
print("Concatenación:", concat)

# 3. Repetición
repetir = cadena1 * 3
print("Repetición:", repetir)

# 4. Acceso a caracteres (indexing)
primer_caracter = cadena1[0]
ulimo_caracter = cadena1[-1]
print("Primer caracter:", primer_caracter, "Último caracter:", ulimo_caracter)

# 5. Subcadenas (slicing)
slice1 = cadena1[0:3]  # primeros 3 caracteres
slice2 = cadena1[1:]   # desde el segundo hasta el final
print("Slice1:", slice1, "Slice2:", slice2)

# 6. Métodos de transformación
titulo = cadena1.title()     # Primera letra mayúscula
mayus = cadena1.upper()      # Todo en mayúsculas
minus = cadena1.lower()      # Todo en minúsculas
capital = cadena1.capitalize() # Solo primera letra mayúscula
strip = '  Hola  '.strip()    # Elimina espacios al inicio y final
print(titulo, mayus, minus, capital, strip)

# 7. Métodos de búsqueda
pos_h = cadena1.find('H')    # Índice de primera aparición, -1 si no existe
count_l = cadena1.count('l') # Número de apariciones
startswith_h = cadena1.startswith('H') # True/False
endswith_a = cadena1.endswith('a')     # True/False
print(pos_h, count_l, startswith_h, endswith_a)

# 8. Métodos de comprobación
isalpha = cadena1.isalpha()   # Solo letras
isdigit = '123'.isdigit()     # Solo dígitos
isalnum = 'abc123'.isalnum()   # Letras o números
isspace = '  '.isspace()       # Solo espacios
print(isalpha, idigit, isalnum, isspace)

# 9. Métodos de reemplazo y división
reemplazo = cadena1.replace('o','0') # Sustituir caracteres
split = concat.split(' ')              # Separar en lista por espacios
join_example = '-'.join(['a','b','c']) # Unir lista con separador
print(reemplazo, split, join_example)

# 10. Métodos de alineación
ljust = cadena1.ljust(10,'*') # Alinea a la izquierda, rellena con '*'
rjust = cadena1.rjust(10,'-') # Alinea a la derecha
center = cadena1.center(10,'+') # Centrado
print(ljust, rjust, center)

# 11. Formateo de cadenas
nombre = 'Juan'
edad = 25
formato1 = 'Hola %s, tienes %d años' % (nombre, edad)  # Antiguo
formato2 = 'Hola {}, tienes {} años'.format(nombre, edad) # Moderno
formato3 = f'Hola {nombre}, tienes {edad} años'          # F-strings (Python 3.6+)
print(formato1, formato2, formato3)

# 12. Escape de caracteres
salto_linea = 'Primera línea\nSegunda línea'
tabulacion = 'Col1\tCol2'
print(salto_linea)
print(tabulacion)

# 13. Métodos de codificación y decodificación
bytes_cadena = cadena1.encode('utf-8')  # Convertir a bytes
cadena_decodificada = bytes_cadena.decode('utf-8')
print(bytes_cadena, cadena_decodificada)

# 14. Comparaciones
igual = 'hola' == 'Hola'  # False (case-sensitive)
mayor = 'b' > 'a'          # True (orden lexicográfico)
print(igual, mayor)

# 15. In y not in
existe = 'H' in cadena1    # True
no_existe = 'x' not in cadena1 # True
print(existe, no_existe)

# 16. Métodos de alineación avanzada (pad y fill)
print(''.center(20,'*'))
print('Python'.ljust(20,'-'))
print('Python'.rjust(20,'_'))

# Fin de referencia completa de cadenas en Python
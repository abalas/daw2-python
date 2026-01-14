# =========================================================
# CHULETA COMPLETÍSIMA: FUNCIONES CON NÚMERO VARIABLE
# DE ARGUMENTOS EN PYTHON (*args y **kwargs)
# =========================================================

# ---------------------------------------------------------
# 1. FUNCIÓN NORMAL (RECORDATORIO)
# ---------------------------------------------------------

def suma(a, b):
    return a + b


# ---------------------------------------------------------
# 2. *args → ARGUMENTOS POSICIONALES VARIABLES
# ---------------------------------------------------------
# *args permite recibir CUALQUIER cantidad de argumentos
# posicionales. Dentro de la función, args es una TUPLA.


def suma_variable(*args):
    total = 0
    for n in args:
        total += n
    return total


print(suma_variable(1, 2))
print(suma_variable(1, 2, 3, 4, 5))


# ---------------------------------------------------------
# 3. *args PUEDE TENER CUALQUIER NOMBRE
# ---------------------------------------------------------
# La convención es usar *args, pero no es obligatorio


def mostrar_valores(*valores):
    for v in valores:
        print(v)


# ---------------------------------------------------------
# 4. **kwargs → ARGUMENTOS CON NOMBRE VARIABLES
# ---------------------------------------------------------
# **kwargs recibe argumentos con nombre
# Dentro de la función, kwargs es un DICCIONARIO


def mostrar_datos(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")


mostrar_datos(nombre="Ana", edad=20, ciudad="Madrid")


# ---------------------------------------------------------
# 5. COMBINAR *args Y **kwargs
# ---------------------------------------------------------
# ORDEN OBLIGATORIO:
# parámetros normales → *args → **kwargs


def funcion_completa(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)


funcion_completa(1, 2, 3, 4, x=10, y=20)


# ---------------------------------------------------------
# 6. *args PARA DESEMPAQUETAR
# ---------------------------------------------------------

numeros = (1, 2, 3)
print(suma_variable(*numeros))  # desempaqueta la tupla


# ---------------------------------------------------------
# 7. **kwargs PARA DESEMPAQUETAR DICCIONARIOS
# ---------------------------------------------------------

persona = {"nombre": "Luis", "edad": 30}
mostrar_datos(**persona)


# ---------------------------------------------------------
# 8. MEZCLAR ARGUMENTOS FIJOS Y VARIABLES
# ---------------------------------------------------------

def saludar(mensaje, *nombres):
    for n in nombres:
        print(mensaje, n)


saludar("Hola", "Ana", "Luis", "Marta")


# ---------------------------------------------------------
# 9. ARGUMENTOS POR DEFECTO + *args
# ---------------------------------------------------------

def multiplicar(*args, factor=1):
    resultado = []
    for n in args:
        resultado.append(n * factor)
    return resultado


print(multiplicar(1, 2, 3, factor=10))


# ---------------------------------------------------------
# 10. FORZAR USO DE **kwargs (KEYWORD-ONLY)
# ---------------------------------------------------------

def configurar(*, debug=False, verbose=False):
    print(debug, verbose)


configurar(debug=True)
# configurar(True, False)  ❌ Error


# ---------------------------------------------------------
# 11. CASO REAL: FUNCIÓN FLEXIBLE
# ---------------------------------------------------------

def crear_usuario(nombre, **datos):
    usuario = {"nombre": nombre}
    usuario.update(datos)
    return usuario


u = crear_usuario("Ana", edad=20, ciudad="Madrid")


# ---------------------------------------------------------
# 12. ERRORES TÍPICOS
# ---------------------------------------------------------
# ❌ Confundir *args con listas
# ❌ Olvidar el orden correcto de parámetros
# ❌ Pasar diccionario sin **
# ❌ Acceder a kwargs como lista


# ---------------------------------------------------------
# 13. TRUCOS DE EXAMEN
# ---------------------------------------------------------
# - *args es una TUPLA
# - **kwargs es un DICCIONARIO
# - El nombre args/kwargs es convención
# - El orden importa
# - Se puede desempaquetar con * y **


# ---------------------------------------------------------
# 14. RESUMEN RÁPIDO
# ---------------------------------------------------------
# *args     → muchos argumentos posicionales
# **kwargs  → muchos argumentos con nombre
# *         → desempaquetar
# **        → desempaquetar diccionarios

# =========================================================
# FIN DE LA CHULETA
# =========================================================

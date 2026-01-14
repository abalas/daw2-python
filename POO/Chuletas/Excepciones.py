# =========================================================
# CHULETA COMPLETÍSIMA: MANEJO DE EXCEPCIONES EN PYTHON
# Archivo de referencia (.py)
# =========================================================

# ---------------------------------------------------------
# 1. QUÉ ES UNA EXCEPCIÓN
# ---------------------------------------------------------
# Una excepción es un error detectado durante la ejecución.
# Permite manejar errores sin que el programa se cierre.

# Ejemplo básico que causa excepción
# 10 / 0  -> ZeroDivisionError


# ---------------------------------------------------------
# 2. BLOQUE TRY / EXCEPT
# ---------------------------------------------------------

try:
    x = int(input("Introduce un número: "))
    y = 10 / x
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except ValueError:
    print("Debes introducir un número válido")


# ---------------------------------------------------------
# 3. EXCEPCIÓN GENÉRICA
# ---------------------------------------------------------

try:
    x = int("hola")
except Exception as e:  # Captura cualquier excepción
    print("Error capturado:", e)


# ---------------------------------------------------------
# 4. BLOQUE ELSE
# ---------------------------------------------------------
# Se ejecuta si no hay excepciones

try:
    x = 5
except Exception:
    print("Error")
else:
    print("Todo correcto, x =", x)


# ---------------------------------------------------------
# 5. BLOQUE FINALLY
# ---------------------------------------------------------
# Siempre se ejecuta, haya o no excepción

try:
    f = open("archivo.txt")
except FileNotFoundError:
    print("Archivo no encontrado")
finally:
    print("Este bloque se ejecuta siempre")


# ---------------------------------------------------------
# 6. LANZAR EXCEPCIONES (raise)
# ---------------------------------------------------------

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

# dividir(5,0)  -> ValueError


# ---------------------------------------------------------
# 7. CREAR EXCEPCIONES PERSONALIZADAS
# ---------------------------------------------------------

class MiError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


def test_personalizado(x):
    if x < 0:
        raise MiError("x no puede ser negativo")


# ---------------------------------------------------------
# 8. ATRIBUTOS DE LA EXCEPCIÓN
# ---------------------------------------------------------

try:
    int("hola")
except ValueError as e:
    print(e.args)      # ('invalid literal for int() with base 10: 'hola',)


# ---------------------------------------------------------
# 9. MÚLTIPLES EXCEPCIONES EN UNA SOLA LÍNEA
# ---------------------------------------------------------

try:
    x = int(input())
except (ValueError, TypeError) as e:
    print("Error tipo ValueError o TypeError", e)


# ---------------------------------------------------------
# 10. EXCEPCIONES ANIDADAS / RE-RAISE
# ---------------------------------------------------------

try:
    try:
        x = 10 / 0
    except ZeroDivisionError as e:
        print("Dentro del inner try")
        raise  # vuelve a lanzar la excepción
except Exception as e:
    print("Capturada afuera:", e)


# ---------------------------------------------------------
# 11. USO EN FUNCIONES
# ---------------------------------------------------------

def leer_entero():
    while True:
        try:
            return int(input("Introduce un número: "))
        except ValueError:
            print("Número inválido, intenta otra vez")


# ---------------------------------------------------------
# 12. LOGGING DE ERRORES
# ---------------------------------------------------------
import logging

logging.basicConfig(level=logging.ERROR)

try:
    1 / 0
except ZeroDivisionError as e:
    logging.error("Se ha producido un error: %s", e)


# ---------------------------------------------------------
# 13. ERRORES TÍPICOS
# ---------------------------------------------------------
# ❌ Capturar Exception siempre y no manejar correctamente
# ❌ Olvidar finally cuando se necesita liberar recursos
# ❌ Lanzar raise sin mensaje útil
# ❌ Mezclar tipos de errores sin control


# ---------------------------------------------------------
# 14. TRUCOS DE EXAMEN
# ---------------------------------------------------------
# - try / except / else / finally
# - raise ValueError("mensaje")
# - Capturar excepción con "as"
# - Crear clases personalizadas heredando de Exception
# - Re-lanzar excepciones con raise

# =========================================================
# FIN DE LA CHULETA DE EXCEPCIONES
# =========================================================

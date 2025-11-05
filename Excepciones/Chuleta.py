# ==========================================================
# 🧾 CHULETA DE EXCEPCIONES EN PYTHON
# ==========================================================
# Autor: [Tu nombre]
# Uso: Archivo de repaso para entender excepciones en Python
# ==========================================================

# ----------------------------------------------------------
# ⚙️ ESTRUCTURA BÁSICA
# ----------------------------------------------------------

try:
    # Código que puede fallar
    x = int(input("Introduce un número: "))
    print(10 / x)
except ZeroDivisionError:
    print("❌ No puedes dividir entre cero")
except ValueError:
    print("❌ Eso no es un número")
except Exception as e:
    print("❌ Error inesperado:", e)
else:
    print("✅ Todo salió bien")
finally:
    print("🔚 Esto se ejecuta siempre")


# ----------------------------------------------------------
# 💣 EXCEPCIONES MÁS COMUNES
# ----------------------------------------------------------
"""
ZeroDivisionError  -> División entre 0
ValueError         -> Conversión de tipo inválida (int("abc"))
TypeError          -> Tipos incompatibles ("a" + 3)
IndexError         -> Índice fuera de rango en una lista
KeyError           -> Clave inexistente en un diccionario
FileNotFoundError  -> Archivo no encontrado
AttributeError     -> Atributo inexistente
AssertionError     -> Fallo en un assert
Exception          -> Cubre todas las excepciones
"""


# ----------------------------------------------------------
# 🚨 USO DE 'raise' PARA LANZAR EXCEPCIONES
# ----------------------------------------------------------

def dividir(a, b):
    """Ejemplo de raise estándar"""
    if b == 0:
        raise ZeroDivisionError("No puedes dividir entre cero")
    return a / b

try:
    dividir(5, 0)
except ZeroDivisionError as e:
    print("Error controlado con raise:", e)


# ----------------------------------------------------------
# 💡 EXCEPCIONES PERSONALIZADAS
# ----------------------------------------------------------

class NumeroNegativoError(Exception):
    """Excepción personalizada para números negativos"""
    pass

def cuadrado(n):
    if n < 0:
        raise NumeroNegativoError("No admito números negativos")
    return n ** 2

try:
    cuadrado(-4)
except NumeroNegativoError as e:
    print("Error personalizado:", e)


# ----------------------------------------------------------
# 🧩 USO DE 'assert' PARA COMPROBACIONES RÁPIDAS
# ----------------------------------------------------------

# 'assert' verifica que una condición se cumpla.
# Si no, lanza AssertionError automáticamente.
# Sintaxis:
# assert condición, "Mensaje si falla"

numero = int(input("Introduce un número positivo: "))
assert numero >= 0, "El número no puede ser negativo"
print("Número válido:", numero)

# Equivale a:
# if not numero >= 0:
#     raise AssertionError("El número no puede ser negativo")


# ----------------------------------------------------------
# 🧠 CUÁNDO USAR CADA UNO
# ----------------------------------------------------------
"""
✅ if + raise   -> Para validar datos del usuario
✅ assert       -> Para comprobaciones internas o pruebas
✅ try/except   -> Para controlar errores externos (archivos, red, etc.)
✅ Excepciones personalizadas -> Para crear tus propios tipos de error
"""


# ----------------------------------------------------------
# 🧰 EJEMPLO COMPLETO
# ----------------------------------------------------------

class EdadInvalidaError(Exception):
    """Error cuando la edad no es válida"""
    pass

def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        assert edad > 0, "La edad debe ser positiva"
        if edad < 18:
            raise EdadInvalidaError("Debes ser mayor de edad")
        print("Edad válida ✅")
    except ValueError:
        print("Debes introducir un número.")
    except AssertionError as e:
        print(e)
    except EdadInvalidaError as e:
        print(e)

# Descomenta para probar:
# pedir_edad()

# ==========================================================
# FIN DE LA CHULETA 🧾
# ==========================================================

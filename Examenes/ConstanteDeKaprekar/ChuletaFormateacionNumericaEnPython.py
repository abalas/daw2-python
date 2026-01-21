# ============================================================
# 🧮 CHULETA DE FORMATEACIÓN NUMÉRICA EN PYTHON
# ============================================================
# Sintaxis general dentro de una f-string:
#    f"{valor:[relleno][alineación][ancho][.precisión][tipo]}"
#
# ------------------------------------------------------------
# 🔢 TIPOS DE FORMATO MÁS COMUNES
# ------------------------------------------------------------
# d → entero decimal
# f → número flotante (decimal)
# e → notación científica (minúsculas)
# E → notación científica (mayúsculas)
# x → hexadecimal (minúsculas)
# X → hexadecimal (mayúsculas)
# % → porcentaje
#
# ------------------------------------------------------------
# 🔹 RELLENAR CON CEROS
print(f"{7:03d}")     # 007   → ancho 3, rellena con ceros

# 🔹 RELLENAR CON ESPACIOS
print(f"{7:3d}")      # '  7' → ancho 3, rellena con espacios

# 🔹 MOSTRAR SIGNO
print(f"{42:+d}")     # +42
print(f"{-42:+d}")    # -42

# 🔹 CONTROLAR DECIMALES
pi = 3.14159265
print(f"{pi:.2f}")    # 3.14
print(f"{pi:.4f}")    # 3.1416

# 🔹 ANCHO Y DECIMALES JUNTOS
print(f"{pi:8.3f}")   # '   3.142' → 8 caracteres de ancho, 3 decimales

# 🔹 NOTACIÓN CIENTÍFICA
print(f"{12345.6789:.2e}")  # 1.23e+04

# 🔹 SEPARADOR DE MILES
print(f"{1234567:,}")  # 1,234,567
print(f"{1234567:_}")  # 1_234_567 (útil para logs o CSVs)

# 🔹 ALINEACIÓN DE NÚMEROS
print(f"{123:<8d}")    # '123     ' → alineado a la izquierda
print(f"{123:^8d}")    # '  123   ' → centrado
print(f"{123:>8d}")    # '     123' → alineado a la derecha

# 🔹 FORMATEAR PORCENTAJE
porcentaje = 0.2578
print(f"{porcentaje:.2%}")  # 25.78%

# 🔹 COMBINAR VARIABLES PARA ANCHO Y PRECISIÓN
ancho = 6
decimales = 3
valor = 9.8765
print(f"{valor:{ancho}.{decimales}f}")  # ' 9.877'

# 🔹 FORMATEAR ENTEROS CON LONGITUD FIJA
codigo = 42
print(f"{codigo:05d}")  # 00042

# ------------------------------------------------------------
# 🧠 RESUMEN RÁPIDO
# ------------------------------------------------------------
# :04d  → Entero con 4 dígitos, relleno con ceros
# :8.2f → Flotante con ancho 8 y 2 decimales
# :>10d → Entero alineado a la derecha con ancho 10
# :<10d → Entero alineado a la izquierda con ancho 10
# :,    → Separador de miles con comas
# :_    → Separador de miles con guiones bajos
# .2f   → Redondea a 2 decimales
# +d    → Muestra siempre el signo
# .2%   → Convierte a porcentaje con 2 decimales
# ============================================================

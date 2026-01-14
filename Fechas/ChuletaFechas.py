"""
=====================================================
CHULETA DATE, TIME, DATETIME y TIMEDELTA - PYTHON
(Equivalente mental a Java: LocalDate, LocalTime,
LocalDateTime)
=====================================================
"""

# ==============================
# 1. IMPORTACIONES
# ==============================
# Todo está en el módulo datetime

from datetime import date, time, datetime, timedelta


# ==============================
# 2. DATE (Solo fecha)
# ==============================
# Equivalente a LocalDate en Java

hoy = date.today()
print("Hoy:", hoy)

# Crear una fecha concreta
cumpleanios = date(1968, 10, 8)
print("Cumpleaños:", cumpleanios)

# Acceso a atributos
print("Año:", hoy.year)
print("Mes:", hoy.month)
print("Día:", hoy.day)


# ==============================
# 3. TIME (Solo hora)
# ==============================
# Equivalente a LocalTime en Java

# Hora por defecto (00:00:00)
despertador = time()
print("Despertador:", despertador)

# Hora concreta
hora_clase = time(8, 30, 0)
print("Hora de clase:", hora_clase)

# Acceso a atributos
print("Hora:", hora_clase.hour)
print("Minuto:", hora_clase.minute)
print("Segundo:", hora_clase.second)


# ==============================
# 4. DATETIME (Fecha + hora)
# ==============================
# Equivalente a LocalDateTime en Java

ahora = datetime.now()
print("Ahora:", ahora)

# Crear fecha y hora concreta
citaMedica = datetime(2025, 12, 15, 17, 15)
print("Cita médica:", citaMedica)

# Acceso a atributos
print("Año:", ahora.year)
print("Mes:", ahora.month)
print("Día:", ahora.day)
print("Hora:", ahora.hour)
print("Minutos:", ahora.minute)
print("Segundos:", ahora.second)


# ==============================
# 5. FORMATEO DE FECHAS (strftime)
# ==============================
# Convierte objetos date/time/datetime a texto

formato_personalizado = ahora.strftime("%A %d-%m-%Y %H:%M:%S")
print("Formato personalizado:", formato_personalizado)

# Formatos comunes
print("Formato completo local (%c):", ahora.strftime("%c"))
print("Solo fecha (%x):", ahora.strftime("%x"))
print("Solo hora (%X):", ahora.strftime("%X"))

# Formatos más usados:
# %Y -> año completo
# %y -> año corto
# %m -> mes (01-12)
# %d -> día (01-31)
# %H -> hora (00-23)
# %M -> minutos
# %S -> segundos
# %A -> día de la semana
# %a -> día semana corto
# %b -> mes abreviado
# %p -> AM / PM
# %j -> día del año
# %W -> semana del año (lunes)
# %U -> semana del año (domingo)


# ==============================
# 6. TEXTO A FECHA (strptime)
# ==============================
# Convierte texto a datetime

cadena = "01-03-2025 14:30:55"
fecha = datetime.strptime(cadena, "%d-%m-%Y %H:%M:%S")
print("Fecha desde texto:", fecha)


# ==============================
# 7. COMPARAR FECHAS
# ==============================
# Igual que en Java: isAfter / isBefore

if ahora > citaMedica:
    print("La fecha actual es POSTERIOR a la cita")
else:
    print("La fecha actual es ANTERIOR a la cita")


# ==============================
# 8. TIMEDELTA (Sumar / restar tiempo)
# ==============================
# Sirve para hacer cálculos con fechas

# Sumar tiempo
nueva_fecha = ahora + timedelta(days=10)
print("Dentro de 10 días:", nueva_fecha)

# Sumar varios valores
nueva_fecha2 = ahora + timedelta(weeks=1, days=10, hours=2)
print("Fecha combinada:", nueva_fecha2)

# Restar fechas (devuelve timedelta)
diferencia = citaMedica - ahora
print("Diferencia entre fechas:", diferencia)


# ==============================
# 9. CONVERSIONES ENTRE TIPOS
# ==============================

# datetime -> date
solo_fecha = ahora.date()
print("Solo fecha:", solo_fecha)

# datetime -> time
solo_hora = ahora.time()
print("Solo hora:", solo_hora)


# ==============================
# 10. RESUMEN RÁPIDO (EXAMEN)
# ==============================
"""
date       -> solo fecha
time       -> solo hora
datetime   -> fecha + hora
timedelta  -> sumar/restar tiempo

strftime() -> objeto a texto
strptime() -> texto a objeto

Las fechas se pueden comparar con:
<  <=  >  >=  ==  !=
"""

# Pedimos al usuario que introduzca los segundos
total_segundos = int(input("Introduce el número de segundos: "))

# Calculamos días, horas, minutos y segundos
dias = total_segundos // 86400
resto = total_segundos % 86400

horas = resto // 3600
resto = resto % 3600

minutos = resto // 60
segundos = resto % 60

# Creamos una lista para almacenar las partes que no son cero
partes = []

if dias > 0:
    partes.append(f"{dias} día{'s' if dias > 1 else ''}")
if horas > 0:
    partes.append(f"{horas} hora{'s' if horas > 1 else ''}")
if minutos > 0:
    partes.append(f"{minutos} minuto{'s' if minutos > 1 else ''}")
if segundos > 0:
    partes.append(f"{segundos} segundo{'s' if segundos > 1 else ''}")

# Mostramos el resultado
resultado = ", ".join(partes)
print(f"Los segundos introducidos equivalen a: {resultado}")

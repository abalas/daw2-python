"""Escribe un programa que le pida al usuario su sueldo anual (lógicamente puede ser
un número con decimales) y le informe que porcentaje de retención le corresponde, el
importe de la misma y el importe neto restante que cobrará."""

sueldo = float(input("Introduce tu sueldo anual en euros: "))

if sueldo <= 12450:
    porcentaje = 19
elif sueldo <= 20199:
    porcentaje = 24
elif sueldo <= 35199:
    porcentaje = 30
elif sueldo <= 59999:
    porcentaje = 37
elif sueldo <= 299999:
    porcentaje = 45
else:
    porcentaje = 47

retencion = sueldo * (porcentaje / 100)
neto = sueldo - retencion

print(f"\nSueldo bruto anual: {sueldo:.2f} €")
print(f"Porcentaje de retención aplicado: {porcentaje}%")
print(f"Importe retenido: {retencion:.2f} €")
print(f"Sueldo neto anual aproximado: {neto:.2f} €")
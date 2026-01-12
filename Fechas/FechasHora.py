"""
En java se usa LocalDate,  LocalTime y LocalDateTime
Hay que hacer un imprort dara, time y datetime
"""
from datetime import date, time, datetime, timedelta
hoy = date.today()
print(hoy)
ahora = datetime.now()
print(ahora)

cumpleanios = date(1968,10,8)
citaMedica = datetime(2025,12,15,17,15)
despertador = time()
print(cumpleanios)
print(citaMedica)
print(despertador)

formateado = ahora.strftime("%A %y-%b-%y - %H:%-M %S %p")
formateado2 =ahora.strftime("(%W) (%U) %a %d-%b-%y (%j) ")
formateado3 = ahora.strftime("%c")
print(formateado3)
formateado3 = ahora.strftime("%x")
print(formateado3)
formateado3 = ahora.strftime("%X")
print(formateado3)
print(formateado)
#falto coger apruntes sobre los diferentes tipos de formatos que se les puede dar

#usar strptime para sacar un objeto de una cadena
cadena = "01-03-2025 14:30:55"
fecha = datetime.strptime(cadena,"%d-%m-%Y %H:%M:%S")
print(fecha)

#como comparar fechas
if ahora > citaMedica:
    print("La fecha de ahora es posterior a cita medica")
else:
    print( "La decha de ahora es anterio a tu cita medica")

print(ahora)
nuevaFecha = ahora +timedelta(days=10, hours=2, weeks=1)
print(nuevaFecha)

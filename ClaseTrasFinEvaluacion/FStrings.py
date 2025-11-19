"""fstring es cadena pero con f delante, no es solamente una cadena, también existen las rStrings"""
def devuelveNombre():
   return "José María"
nombre=("José María")
edad = 57
sueldo = 10000.556
print("Mi nobre %s, tengo %d años y cobro %.2f eruros al mes" %(nombre, edad, 10000.556))
print(f"Mi nombre {nombre}, tengo {edad} años y combro {sueldo :.2f} euros al mes")
ratio = 0.08394
print(f"Porcentaje: {ratio:.1%}")
habitantes = 7123456789
print(f"Poblacion: {habitantes:,} habitantes")
num1=45
num2=123
print(f"{num1: 04d}\n{num2: 04d}")
texto="Python"
print(f"***{texto:<20}***")
print(f"***{texto:>20}***")
print(f"***{texto:^20}***")
print(f"{num1=}\n{num2=}")
texto = f"{num1=}\n{num2=}"
print(texto)
#Varias lineas
ficha = f"""
Ficha del profesor/a:
=====================
Nombre: {devuelveNombre()}
Edad: {edad} años
Salario: {sueldo:.2f} {{euros}}euros
"""
print(ficha)

numero = 33
print(f"""¿numero es par? {'veradero' if numero%2==0 
else 'falso' }""")
print(texto)
print(f"Valoracion: {'Alto' if numero > 50 else 'Medio' if numero <25 else 'Bajo'}")
print(f"{35*1000}")
lista= ("1","2")
print(",".join(lista))
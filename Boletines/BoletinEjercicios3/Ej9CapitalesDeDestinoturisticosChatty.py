"""Escribir un programa que nos pida elegir entre cuatro destinos turísticos (Francia,
Italia, Chile o Japón) y dependiendo de nuestra respuesta nos diga cual es la capital de
nuestro destino (París, Roma, Santiago de Chile o Tokio)"""
eleccion = int(input(f""" Eligue destino turistico:
1. Francia
2. Italia
3. Chile
4. Japón 
Elige (1-4)
"""))
destinoTuristico = { 1:"París", 2:"Roma", 3:"Santiago de Chile", 4:"Tokio"}
print(destinoTuristico.get(eleccion), "Opcion no valida")

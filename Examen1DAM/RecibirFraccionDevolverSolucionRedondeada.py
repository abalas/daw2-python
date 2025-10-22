# Ejercicio 4: Recibir una fracción y devolver solución redondeada a 3 decimales
while True:
    fraccion = input("Escribe tu fracción: ")

    # Comprobaciones básicas
    if fraccion.count('/') != 1:
        print("Error: La fracción debe tener exactamente una barra '/'.")
        continue
    if fraccion.startswith('/') or fraccion.endswith('/'):
        print("Error: La barra '/' no puede estar al inicio ni al final.")
        continue
    numerador, denominador = fraccion.split('/')
    if not numerador.isdigit() or not denominador.isdigit():
        print("Error: Solo se permiten números enteros en la fracción.")
        continue
    numerador = int(numerador)
    denominador = int(denominador)
    if denominador == 0:
        print("Error: El denominador no puede ser 0.")
        continue

    # Si pasa todas las comprobaciones, calcular resultado
    resultado = round(numerador / denominador, 3)
    print(f"Solución: {resultado}")
    break

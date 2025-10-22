# Ejercicio 3: Recibir texto y eliminar espacios y vocales
texto = input("Escribe un texto:")

vocales = 'aeiouAEIOU'
texto_sin = ''
vocales_suprimidas = 0
espacios_suprimidos = 0

for c in texto:
    if c in vocales:
        vocales_suprimidas += 1
    elif c == ' ':
        espacios_suprimidos += 1
    else:
        texto_sin += c

print(f"Sin vocales ni espacios: {texto_sin}")
print(f"Vocales suprimidas: {vocales_suprimidas}")
print(f"Espacios en blanco suprimidos: {espacios_suprimidos}")

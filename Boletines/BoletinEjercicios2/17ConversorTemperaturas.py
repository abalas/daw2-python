def deCelciusAFarenheit(c):
    f = c * 1.8 + 32
    return f

def deFarenheitACelcius(f):
    c = (f - 32) / 1.8
    return c

def deKelvinACelcius(k):
    c = k - 273.15
    return c

def deCelciusAKelvin(c):
    k = c + 273.15
    return k

def deFarenheitAKelvin(f):
    k = (5 / 9) * (f - 32) + 273.15
    return k

def deKelvinAFarenheit(k):
    f = 1.8 * (k - 273.15) + 32
    return f

def imprimeResultados(c, f, k):
    print(f"{c:.2f} ºC")
    print(f"{f:.2f} ºF")
    print(f"{k:.2f} ºK")


entrada = input("Introduzca una medida de temperatura: ")
numero = ""
unidad = ""

for char in entrada:
    if char.isdigit() or char == ".":
        numero += char
    else:
        unidad += char.upper()

numero = float(numero)

if unidad == "C":
    c = numero
    k = deCelciusAKelvin(c)
    f = deCelciusAFarenheit(c)
    imprimeResultados(c, f, k)

elif unidad == "K":
    k = numero
    c = deKelvinACelcius(k)
    f = deKelvinAFarenheit(k)
    imprimeResultados(c, f, k)

elif unidad == "F":
    f = numero
    c = deFarenheitACelcius(f)
    k = deFarenheitAKelvin(f)
    imprimeResultados(c, f, k)

else:
    print("Unidad no válida. Use C, F o K.")
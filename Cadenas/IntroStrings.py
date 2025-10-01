
texto = "Hola mundo"
print(texto[2:-2:1]) #slices, rebanadas
print(texto[::-1])

texto2 = "Hola" + " mundo" + "cruel"
texto3 = "hola" , "mundo", "cruel"
numero = 10
print(texto)
print("Hola", "mundo", "cruel")
print("Hola" + "mundo" + "cruel" + str(numero))
for caracter in texto:
    print(caracter, end="-")
    print("\n", len(texto))

for posicion in range(0,len(texto)):
    print(posicion, "-", texto[posicion])


print(texto.upper())
print(texto.lower())
print(texto.swapcase())


print(texto.find("un"))
print(texto.count("o"))
print(texto.replace("do","X"))
print(texto.find("o",2, len(texto)))

print(texto.replace(" ", "X"))
print(texto.replace(" ", "X", 1))
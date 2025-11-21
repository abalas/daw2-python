frase = input("Introduzca una frase")
fraseAlReves = ""
if(frase.isalpha()):
    for i in range(len(frase)-1,-1,-1):
        fraseAlReves+=frase[i]
print(fraseAlReves)

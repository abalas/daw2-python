frase= input("Introduzca una frase:")
contEspacios=0

fraseSinEspacios=""
for i in frase:
    if(i==" "):
        contEspacios +=1;
    else:
        fraseSinEspacios += i

print(f"Numero de espacios: {contEspacios}")
print(f"Frase sin espacios: {fraseSinEspacios}")
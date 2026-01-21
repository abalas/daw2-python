def calculoConstKepler(numero):
    numero = str(numero)
    nAscendente = sorted(numero)
    nAscendente = str("".join(nAscendente))
    print(nAscendente)
    nDescendente = sorted(numero, reverse=True)
    nDescendente = str("".join(nDescendente))
    print(nDescendente)
    resultado= int(nDescendente) - int(nAscendente)
    print(f"${nDescendente} - ${nAscendente} = ${resultado}")
    return resultado



numeroValido= False

while(numeroValido==False):
    numero = input("Introduce un numero de 4 cifras con cada digito distinto entre si: ")
    if(len(numero)!=4):
        pass
    else:
        numeroSinRepeticion = set(numero)
        if(len(numeroSinRepeticion)!=4):
            pass
        else:
            if numero.isdigit():
                numeroValido=True
#Una vez validada la entada tenemos que ordenar en dos variables de forma ascendente y descendente
#numero = int(numero)
contador = 1
numero = calculoConstKepler(numero)
while(numero!=6174):
    numero = calculoConstKepler(numero)
    contador += 1
print("Ha llevado ", contador, " operaciones")



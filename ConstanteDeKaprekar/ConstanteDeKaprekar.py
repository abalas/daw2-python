def calculoConstKepler(numero):
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
while(calculoConstKepler(numero)!=6137):
    contador += 1
    pass
print("Ha llevado ", contador, " operaciones")



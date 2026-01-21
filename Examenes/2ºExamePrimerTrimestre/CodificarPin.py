from sympy.solvers.ode.ode import sysode_linear_2eq_order1
def devuelveCodigo(n):
    lista = list("XXXXXXXXXX")
    lista_aux = (lista).copy()
    numero = f"{n:04d}"
    resultados= list()

    for i in range (0,len(numero)):
        cont = 0;
        for j in range(0,int(numero[i])):
            lista[len(lista)-int(numero[i])-cont]="O"
            cont -= 1
        resultados.append("".join(lista))
        lista= lista_aux.copy()
    return(tuple(resultados))


pin = int(input("Introduzca su pin:"))
tupla = devuelveCodigo(pin)
contador = 0
for i in tupla:
    print(tupla[contador])
    contador +=1


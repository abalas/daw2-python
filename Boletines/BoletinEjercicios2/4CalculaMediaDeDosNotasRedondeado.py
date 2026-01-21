nota1 = float(input("Introduzca la  primera nota"))
if nota1 < 0 or nota1 > 10:
    print("Entrada incorrecta. No se puede realizar el calculo")
else:
    nota2 = float(input("Introduzca la  segunda nota"))
    if nota1 < 0 or nota1 > 10:
        print("Entrada incorrecta. No se puede realizar el calculo")
    else:
        media = (nota1 + nota2)/2
        print("La media de las dos notas sin decimales es: " + str(round(media)))


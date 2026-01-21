"""Escribir un programa que pida números entre el 1 y el 100 por teclado hasta que
escribamos la palabra FIN (con mayúsculas). Si el usuario introduce una entrada
inválida (números superiores a 100, otras cadenas de caracteres que no sean FIN, etc.)
no se tendrá en cuenta pero se mostrará un mensaje de error y el programa seguirá
su curso. Cuando terminamos (al introducir la palabra FIN, recuerda) mostraremos por
 pantalla el numero de entradas válidas que hemos hecho (sin contar esta última
que sólo sirve para finalizar el programa)"""

finalizado = False
cont_entradas_validas = 0
cont_entradas_invalidas = 0
max = 0
min = 0

while not finalizado:
    entrada = input("Introduzca un numero del 1 al 100 o FIN para terminar el programa: ")

    if entrada == "FIN":
        finalizado = True

    else:
        if entrada.isdigit():
            i
        if entrada.isdigit() and int(entrada)>0 and int(entrada)<101:
            cont_entradas_validas +=1
        else:
            cont_entradas_invalidas +=1
            print("Error")
print(f"Numero de entradas validas: {cont_entradas_validas}")
print(f"Numero entradas invalidas: {cont_entradas_invalidas}")
print(f"entradas totales: {cont_entradas_invalidas+cont_entradas_validas}")
print(f"Porcentaje de entradas validas: ", cont_entradas_validas/(cont_entradas_invalidas+cont_entradas_invalidas))



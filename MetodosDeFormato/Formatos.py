texto = "33.5"    #is digit devuelve true si todos los caracteres de la cadena son digitos
if texto.isdigit() == True:
    print("Puedo convertirlo a entrero")
else:
    print("Si tiene números")

texto = "P"  #Alpha es para ver si todos son caracteres alpanumericos
if texto.isalpha() == True:
    print("Puedo convertirlo a entrero")
else:
    print("Si tiene números")
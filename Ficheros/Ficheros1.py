try:
    fichero = open("quijote.txt", "r+")
    print(fichero.readline())
    print("Despues de leer estoy aquí: ",fichero.tell())
    fichero.write("XXX")
    print(fichero.tell())
    fichero.seek(0)# cuando se cambia entre lectura y escritura el cursor pierde su posicion
    #seek(0)--> inicio
    #seek(0,2) --> FIN
    #seek(n) -> psicicion n contando desde el principio
    fichero.seek(fichero.tell()+10) #para moverse diez posiciones de donde estas

    fichero.close()

except:
    print("Error al manipular el fichero")
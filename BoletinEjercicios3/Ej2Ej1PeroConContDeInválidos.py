
contrasenia1 = input("Introduzca la contraseña: ")
contrasenia2 = input("Vuelva a intriducir su contrasenia: ")
contIntentos = 0

while(contrasenia1!=contrasenia2):
    print("Contraseña inválida. Intruduzcalas de nuevo")
    contIntentos +=1
    contrasenia1 = input("Introduzca la contraseña: ")
    contrasenia2 = input("Vuelva a intriducir su contrasenia: ")
print("Contraseña guardada")
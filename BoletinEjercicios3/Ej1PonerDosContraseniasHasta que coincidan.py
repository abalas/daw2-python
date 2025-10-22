
contrasenia1 = input("Introduzca la contraseña: ")
contrasenia2 = input("Vuelva a intriducir su contrasenia: ")

while(contrasenia1!=contrasenia2):
    print("Contraseña inválida. Intruduzcalas de nuevo")
    contrasenia1 = input("Introduzca la contraseña: ")
    contrasenia2 = input("Vuelva a intriducir su contrasenia: ")
print("Contraseña guardada")
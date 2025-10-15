n = int(input("Introduzca un numero y le dareé su tabla de multiplicar: "))
print("Tabla de multiplicar del: " + n)
for i in range(0,11):
    print(f"{n} x {i} = {n*i}")
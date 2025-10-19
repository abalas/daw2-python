""""Escribe un programa que pida por teclado el radio de una circunferencia, admitiendo
valores con decimales y calcule la longitud y el área de la circunferencia (redondeando
a cinco decimales). Si no las recuerdas, las fórmulas son las siguientes:  3.14159"""
radio = float(input("Introduzca un el radio de la circunferencia: "))
area = (radio**2 *  3.14159)
perimetro = (radio*2 *  3.14159)


print(f"Tu perímetro es de {perimetro}cm " )
print(f"Tu perímetro es de {area}cm cuadrados " )
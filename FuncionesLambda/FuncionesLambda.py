"""Caracteristicas de una funcion lambda:
Que son anonimas y no tiene  noombre aunque van asignadas a un acvariables
Solo una instruccion  esa intruccion genera un valor que devuelve la funcion"""

def cuadrado(x):
    return x**2
print(cuadrado(25))

cuadradoLambda = lambda x:x**2

print(cuadradoLambda(25))

sumaLambda = lambda x,y,z: x+y+z
print(sumaLambda(1,2,3))

media = lambda *lista:sum(lista)/len(lista)
print(media(3,5,6,1,2,3,4,5,6,7,8,9))
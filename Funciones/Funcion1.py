def miFuncion():
    print("Hola mundo")
def saludo(nombre, despedida):
    return "Hola " + nombre + despedida
def funcion(valor):
    valor*=5
    print(valor)

def saludo2(nombre="Rafael", despedida=" Te veo pronto!"):
    print("Vamos allá")
    return "Hola " + nombre + despedida

miFuncion()
nombre = " José maría"
print(saludo(nombre, " que te vaya bien"))

def devuelveNumeros():
    return 1,2,3
n1, n2, n3 = devuelveNumeros()
print(n1, n2, n3, sep="-")

n = 2
funcion(n)

print(saludo2(nombre, "Que te vaya bien"))
print(saludo2(despedida= "Adios, adios", nombre="Luis"))
print(saludo("manuel", "Que te vaya bonito"))

def muestraProfes(veces=1,*nombres):
    for _ in range(veces):
        for n in nombres:
            print(n)

muestraProfes(2,"Natalia","Agustin")
muestraProfes(2,"Pedro",2,"Ana")

def repiteNombre(veces=1,*nombres):
    for _ in range(veces):
        for n in nombres:
            print(n)
datos = [2, "Pepe"]
datos2 = [4, "Luis"]
repiteNombre(*datos)
repiteNombre(*datos)
repiteNombre(*[3, "Eva"])


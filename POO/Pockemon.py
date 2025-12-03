import random
class Pockemon:
    def __init__(self,codigo, nombre, evolucion=None):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__evolucion = evolucion
        self.__pv = random.randint(50,100)

    def mostrarDatos(self):
        print(f""""
        ======| Ficha datos de {self.__nombre} |======
        | Nº pockedex: {self.__codigo}                |
        | PV: {self.__pv}                             |
        | Evoluciona en:{self.__evolucion.__nombre}     |
        ===============================================
""")
    def evoluciona(self):
        if self.__evolucion == None:
            evo = self
            print("Este pockemon no sabe evolucionar")
        else:
            evo = self.__evolucion
        return evo
    def combateContra(self,contrincante):
        if self.__pv >0 and contrincante.__pv >0:
            while contrincante.__pv>0 and self.__pv>0:
                danyo = random.randint(25,75)
                contrincante.__pv -= danyo
                if contrincante.__pv <=0:
                    print(contrincante.__nombre, " ha sido derrotado, has ganado el combate")
                else:
                    danyo = random.randint(25, 75)
                    self.__pv -= danyo
                    if self.__pv<=0:
                        print(self.__nombre, " ha sido derrotado, has perdido el combate")
        else:
            print("No esta en condiciones de luchar")



p3 = Pockemon(1,"Bulbasur")
p2 = Pockemon(2, "Venosaur", p3)
p1 = Pockemon(1, "Bulbasur", p2)

p1.mostrarDatos()

p1.combateContra(p3)



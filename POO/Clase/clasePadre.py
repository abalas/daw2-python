class Padre:
    def __init__(self):
        self._titulo = "Soy la clase Padre" #_Padre__titulo
    def mostrar(self):
        print("PPP",self._titulo) #_Padre__titulo
class Madre:
    def __init__(self):
        self.titulo= "Soy la calse Madre"
    def mostrar(self):
        print("MMM", self.titulo)
class Hijo(Madre,Padre):
    def __init__(self):
        self._titulo = "Soy la clase Hijo" #_Hijo__titulo
    def mostrar(self, mensaje):
        #Padre.mostrar(self)    esta forma de escribirlo hace que cuando haya herencia multiple tenga prioridad la clase que pongas
        super().mostrar()
        print(mensaje)

objeto1 = Padre()
objeto1.mostrar()

objeto2 = Hijo()
objeto2.mostrar("Hola soy la clase Hijo")
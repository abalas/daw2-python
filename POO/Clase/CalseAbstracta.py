from abc import abstractmethod, ABCMeta


class Abstracta(metaclass=ABCMeta):
    def metodoNormal(self):
        print("Hola mundo")

    @abstractmethod
    def metodoAbstarcto(self):
        pass
class Hija(Abstracta):
    def metodoAbstracto(self):
        print("Adios Mundo")


elemento = Hija()
elemento.metodoNormal()
elemento.metodoAbstracto()
profesores = ["Jose Maria", "Natalia", "Agustín"]
iterador = iter(profesores,"Stop")
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

class DiasDeLaSemana:
    def __init__(self, dia=0):
        self.dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
        self.dia = dia
    def __iter__(self):
        return self
    def __next__(self, stop=None):
        if self.dia>=len(self.dias):
            if stop==None:
                raise StopIteration
            else:
                print(stop)
        dia_actual = self.dias[self.dia]
        self.dia+=1
        return dia_actual
    def __next__(self, stop=None):
        dia_actual = self.dias[self.dia]
        if self.dia == 6:
            self.dia=0
        return dia_actual


semana = DiasDeLaSemana
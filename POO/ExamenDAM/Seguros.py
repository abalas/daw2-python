from datetime import date
from abc import ABC, abstractmethod


class Conductor:
    def __init__(self, nombre, edad, anos_carnet, puntos):
        self.nombre = nombre
        self.edad = edad
        self.anos_carnet = anos_carnet
        self.puntos = puntos


class Vehiculo(ABC):
    def __init__(self, matricula, ano_compra, conductor):
        self.matricula = matricula
        self.ano_compra = ano_compra
        self.conductor = conductor

    def antiguedad(self):
        return date.today().year - self.ano_compra

    @abstractmethod
    def seguro_terceros(self):
        pass

    @abstractmethod
    def seguro_todo_riesgo(self):
        pass


class Coche(Vehiculo):
    def seguro_todo_riesgo(self):
        edad = self.antiguedad()

        if edad == 1:
            precio = 400
        elif edad == 2:
            precio = 500
        elif edad == 3:
            precio = 700
        else:
            precio = edad * 250

        if self.conductor.puntos < 8:
            precio += 100

        return precio

    def seguro_terceros(self):
        precio = 250

        if self.conductor.puntos < 8:
            precio += 100
        if self.conductor.edad < 24:
            precio += 50
        if self.conductor.anos_carnet < 2:
            precio += 75

        return precio


class Moto(Vehiculo):
    def seguro_todo_riesgo(self):
        return None

    def seguro_terceros(self):
        precio = 200

        if self.conductor.puntos < 8:
            precio += 150
        if self.conductor.edad < 24:
            precio += 25
        if self.conductor.anos_carnet < 2:
            precio += 50

        return precio

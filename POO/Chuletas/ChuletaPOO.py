# =========================================================
# CHULETA COMPLETA DE PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
# EN PYTHON
# Basada en apuntes de clase + ampliación y correcciones
# =========================================================

# ---------------------------------------------------------
# 1. CLASES Y OBJETOS
# ---------------------------------------------------------

class Persona:
    """Ejemplo básico de clase"""

    def __init__(self, nombre, edad):  # Constructor
        self.nombre = nombre           # Atributo de instancia
        self.edad = edad

    def saludar(self):                 # Método
        print(f"Hola, me llamo {self.nombre}")


p = Persona("Ana", 20)
p.saludar()


# ---------------------------------------------------------
# 2. ATRIBUTOS DE CLASE VS INSTANCIA
# ---------------------------------------------------------

class Alumno:
    instituto = "IES Python"          # Atributo de clase (compartido)

    def __init__(self, nombre):
        self.nombre = nombre           # Atributo de instancia


a1 = Alumno("Luis")
a2 = Alumno("Marta")


# ---------------------------------------------------------
# 3. ENCAPSULACIÓN
# ---------------------------------------------------------

class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo            # Convención: protegido
        self.__clave = "1234"          # Privado (name mangling)

    def mostrar_saldo(self):
        return self._saldo


# ---------------------------------------------------------
# 4. HERENCIA
# ---------------------------------------------------------

class Animal:
    def hablar(self):
        print("El animal hace un sonido")


class Perro(Animal):
    def hablar(self):                  # Polimorfismo
        print("Guau")


# ---------------------------------------------------------
# 5. SUPER()
# ---------------------------------------------------------

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca


class Coche(Vehiculo):
    def __init__(self, marca, puertas):
        super().__init__(marca)        # Llama al constructor padre
        self.puertas = puertas


# ---------------------------------------------------------
# 6. CLASES ABSTRACTAS (FORMA EXPLÍCITA - APUNTES)
# ---------------------------------------------------------

from abc import ABCMeta, abstractmethod

class Abstracta(metaclass=ABCMeta):
    def metodoNormal(self):
        print("Hola mundo")

    @abstractmethod
    def metodoAbstracto(self):
        pass


class Hija(Abstracta):
    def metodoAbstracto(self):
        print("Adiós Mundo")


elemento = Hija()
elemento.metodoNormal()
elemento.metodoAbstracto()

# NOTA:
# No se puede instanciar una clase abstracta
# Abstracta()  --> TypeError


# ---------------------------------------------------------
# 7. CLASES ABSTRACTAS (FORMA MODERNA RECOMENDADA)
# ---------------------------------------------------------

from abc import ABC

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


# ---------------------------------------------------------
# 8. POLIMORFISMO
# ---------------------------------------------------------

figuras = [Cuadrado(2), Cuadrado(5)]

for f in figuras:
    print(f.area())


# ---------------------------------------------------------
# 9. ITERADORES Y ITERABLES (APUNTES + CORRECCIÓN)
# ---------------------------------------------------------

profesores = ["Jose Maria", "Natalia", "Agustín"]

# Iterador manual
it = iter(profesores)
print(next(it))
print(next(it))
print(next(it))
# next(it)  -> StopIteration


# ---------------------------------------------------------
# 10. CLASE ITERABLE PERSONALIZADA
# ---------------------------------------------------------

class DiasDeLaSemana:
    def __init__(self):
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves",
                     "Viernes", "Sábado", "Domingo"]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.dias):
            raise StopIteration
        dia = self.dias[self.index]
        self.index += 1
        return dia


for dia in DiasDeLaSemana():
    print(dia)


# ---------------------------------------------------------
# 11. BUENAS PRÁCTICAS
# ---------------------------------------------------------
# - Usar nombres claros y consistentes
# - No repetir código (DRY)
# - Usar clases abstractas como contratos
# - Preferir ABC sobre ABCMeta directamente
# - Un método abstracto debe implementarse EXACTAMENTE igual


# ---------------------------------------------------------
# 12. ERRORES TÍPICOS
# ---------------------------------------------------------
# ❌ Error de nombre en método abstracto
# ❌ Instanciar una clase abstracta
# ❌ No llamar a super() cuando es necesario
# ❌ Confundir iterable con iterador

# =========================================================
# FIN DE LA CHULETA
# =========================================================

class CuentaCorriente:
    __numCuentas = 0
    """ _codigo -> protected
        __saldo -> privado
        _titular -> protegido (lista de titulares)
    """
    def __init__(self, codigo, titular, saldo=500):
        self._codigo = codigo          # protected
        self._titular = []             # protected: lista de titulares
        self._titular.append(titular)  # se añade el primer titular
        self.__saldo = saldo           # private
        CuentaCorriente.__numCuentas += 1

    # setter manual
    def setSaldo(self, saldo):
        self.__saldo = saldo

    # ---- Property para saldo ----
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    # -----------------------------

    @classmethod
    def getNumCuentas(cls):
        return cls.__numCuentas

    @staticmethod
    def devolverDatosSucursal():
        print("Calle del Pez, 7. 28032. Madrid")

    def __str__(self):
        return f"{self._codigo} - {self._titular} - Saldo: {self.__saldo}"

    # operador suma de cuentas
    def __add__(self, otra):
        nueva = CuentaCorriente(
            self._codigo,
            self._titular[0],
            self.__saldo + otra._CuentaCorriente__saldo
        )
        # fusionar titulares
        nueva._titular = self._titular + otra._titular
        return nueva


# Crear objetos
c1 = CuentaCorriente(2467, "José María Morales", 10000.55)
c2 = CuentaCorriente(23468, "Kevin Aguilera")

# Modificar saldo
c2.setSaldo(69.69)

# Imprimir número de cuentas
print(CuentaCorriente._CuentaCorriente__numCuentas)
print(CuentaCorriente.getNumCuentas())

# Métodos estáticos
c2.devolverDatosSucursal()
CuentaCorriente.devolverDatosSucursal()

# Acceso protegido y privado
print(c1._titular)
print(c1._CuentaCorriente__saldo)

# Property
c2.saldo = 1500
print(c2.saldo)

# records
class Alumno:
    pass

alumno1 = Alumno()
alumno1.nombre = "Juan"
alumno1.apellido = "Balas"
alumno1.edad = 24
alumno1.telefono = 655223344

print(str(c1))
print(c1.__str__())

# Usar __add__
c1 = c1 + c2
print(str(c1))




""" dunder 
__init__
__del__
__str__
__len__

__ad__
__sub__
__mul__
__truediv__

__eq__
__ne__
__gt__
__it__

__iter__
__next__
"""
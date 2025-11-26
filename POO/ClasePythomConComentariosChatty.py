class CuentaCorriente:
    """
    Clase que representa una cuenta bancaria simple con:
    - Código de cuenta (protegido)
    - Titulares (lista protegida)
    - Saldo (privado)

    También lleva un recuento de cuántas cuentas han sido creadas.
    """

    __numCuentas = 0  # Atributo de clase (privado): contador total de cuentas

    def __init__(self, codigo: int, titular: str, saldo: float = 500.0):
        """
        Constructor de la clase.
        :param codigo: Código identificador de la cuenta
        :param titular: Nombre del titular principal
        :param saldo: Saldo inicial (por defecto 500)
        """
        self._codigo = codigo  # Atributo protegido
        self._titular = [titular]  # Lista protegida de titulares
        self.__saldo = saldo  # Atributo privado

        CuentaCorriente.__numCuentas += 1  # Incrementar contador global

    # ---------------------- GETTERS / SETTERS MODERNOS ----------------------

    @property
    def saldo(self) -> float:
        """Getter del saldo (lectura controlada)."""
        return self.__saldo

    @saldo.setter
    def saldo(self, nuevo_saldo: float):
        """
        Setter del saldo, permite validación.
        :param nuevo_saldo: Nuevo saldo de la cuenta
        """
        if nuevo_saldo < 0:
            raise ValueError("El saldo no puede ser negativo.")
        self.__saldo = nuevo_saldo

    # Setter clásico (innecesario, pero válido para aprender)
    def setSaldo(self, saldo: float):
        self.__saldo = saldo

    # ---------------------- MÉTODOS DE CLASE Y ESTÁTICOS ----------------------

    @classmethod
    def getNumCuentas(cls) -> int:
        """Devuelve cuántas cuentas han sido creadas."""
        return cls.__numCuentas

    @staticmethod
    def devolverDatosSucursal():
        """Información general de la sucursal (no depende de ninguna cuenta)."""
        print("Sucursal: Calle del Pez, 7. 28032. Madrid")

    # ---------------------- REPRESENTACIÓN DE OBJETOS ----------------------

    def __str__(self) -> str:
        """Representación legible del objeto."""
        return f"Cuenta {self._codigo} | Titulares: {self._titular} | Saldo: {self.__saldo}€"

    # ---------------------- OPERADOR + ENTRE CUENTAS ----------------------

    def __add__(self, otra: "CuentaCorriente") -> "CuentaCorriente":
        """
        Suma dos cuentas creando una nueva:
        - Suma los saldos
        - Fusiona las listas de titulares
        """
        nueva = CuentaCorriente(
            self._codigo,
            self._titular[0],
            self.__saldo + otra._CuentaCorriente__saldo  # name mangling
        )

        # Unimos titulares de ambas cuentas
        nueva._titular = self._titular + otra._titular

        return nueva


# --------------------------------------------
# EJEMPLOS DE USO (código de prueba)
# --------------------------------------------

# Crear objetos
c1 = CuentaCorriente(2467, "José María Morales", 10000.55)
c2 = CuentaCorriente(23468, "Kevin Aguilera")

# Modificar saldo mediante setter clásico
c2.setSaldo(69.69)

# Número total de cuentas creadas
print("Número de cuentas:", CuentaCorriente.getNumCuentas())

# Ejecutar método estático
CuentaCorriente.devolverDatosSucursal()

# Acceso protegido (permitido pero no recomendado)
print("Titulares de c1:", c1._titular)

# Acceso a atributo privado mediante name mangling (NO recomendado, pero válido para aprender)
print("Saldo privado de c1:", c1._CuentaCorriente__saldo)

# Modificar saldo mediante property
c2.saldo = 1500
print("Nuevo saldo c2:", c2.saldo)


# Crear un objeto tipo "record"
class Alumno:
    pass


alumno1 = Alumno()
alumno1.nombre = "Juan"
alumno1.apellido = "Balas"
alumno1.edad = 24
alumno1.telefono = 655223344

# Mostrar cuenta con __str__
print(str(c1))

# Operador suma entre cuentas
c1 = c1 + c2
print("Cuenta fusionada:", c1)

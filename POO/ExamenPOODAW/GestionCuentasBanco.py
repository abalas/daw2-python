

class Sucursal:
    def __init__(self, direccion, provincia, codigoID):
        self.direccion = direccion
        self.provincia = provincia
        self.codigoID = codigoID
        self.cuentas = []

    def aniadirCuenta(self, cuenta):
        self.cuentas.append(cuenta)
    def devolverCuentas(self):
        saldoTotal = 0;
        relleno = "ES68 1234"
        cadena = f"""Cuentas de la sucursal {self.codigoID} ({self.provincia})
"""
        for i in self.cuentas:
            cadena += f"""
{relleno} {self.codigoID} {i.codigo12} - Saldo: {i.saldo}€"""
            saldoTotal += int(i.saldo)
        cadena += f"""
Saldo total: """ + str(saldoTotal)

        print(cadena)

class Cliente:
    def __init__(self, nombre, apellidos, nif, telefono, sucursal ):
        self.nombre = nombre
        self.apellidos = apellidos
        self.nif = nif
        self.telefono = telefono
        self.sucursal = sucursal
        self.cuentas = []

    def aniadirCuenta(self, cuenta):
        self.cuentas=cuenta
    def devolverCuentas(self):
        saldoTotal = 0;
        relleno = "ES68 1234"

        for i in self.cuentas:
            cadena = f"""
{self.nombre} {self.apellidos}. Cliente de la sucursal {self.sucursal.codigoID} ({self.sucursal.provinciaprovincia}  - Saldo: {i.saldo}€)
            """
            saldoTotal += int(i.saldo)
        cadena += f"""
Saldo total: """ + str(saldoTotal)

        print(cadena)

class CuentaCorriente:
    def __init__(self, codigo12, saldo, titularesDeLaCuenta, sucursal ):
        self.codigo12 = codigo12
        self.saldo = saldo
        self.titularesDeLaCuenta = titularesDeLaCuenta
        self.sucursal = sucursal


sucursal1 = Sucursal("Plaza De España", "Madrid", "0001" )
sucursal2 = Sucursal("Plaza De Cataluña", "Barcelona", "0002" )



pedro = Cliente("Pedro", "Sanchez", "X0392117Y", "60000001", sucursal1)
maria = Cliente("Maria", "Gomez", "X0000000X", "600000002", sucursal1)
juanito = Cliente("juan","gomez", "X0000000X", "600000001", sucursal1)



cc1 = CuentaCorriente( "123456789012", "1000", pedro, sucursal1 )
cc2 = CuentaCorriente( "123456789013", "1050", maria, sucursal1 )
cc3 = CuentaCorriente( "123456789014", "20000", juanito, sucursal1 )

sucursal1.aniadirCuenta(cc1)
sucursal1.aniadirCuenta(cc2)
sucursal1.aniadirCuenta(cc3)
sucursal1.devolverCuentas()

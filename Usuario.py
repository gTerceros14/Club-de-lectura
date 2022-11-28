from Persona import *
class Usuario(Persona):
    def __init__(self, nombrePersona, apellidoPersona, nombreUsuario, CI, contrasenia, edad, cuentaBancaria, saldoLibros, subscripcionMensual, librosComprados):
        super().__init__(nombrePersona, apellidoPersona, nombreUsuario, CI, contrasenia, edad)
        self._cuentaBancaria = cuentaBancaria
        self._saldoLibros = saldoLibros
        self._subscripcionMensual = subscripcionMensual
        self._librosComprados = librosComprados
    
    def __str__(self) -> str:
        return super().__str__() + '\nCuenta bancaria: ' + str(self._cuentaBancaria) + '\nSaldo libros: ' + str(self._saldoLibros) + '\nSubscripcion Mensual: ' + str(self._subscripcionMensual) + '\nLibros comprados: ' + str(self._librosComprados)

from codigos.Personas import Personas
class Usuario(Personas):
    def __init__(self,nombre,apellido,ci,cuentaBancaria,nomUsuario,contrasenia):
        super().__init__(nombre,apellido,ci)
        self._cuentaBancaria=cuentaBancaria
        self._nomUsuario=nomUsuario
        self._contrasenia=contrasenia
    def __str__(self):
        return super().__str__()+"\n:Cuenta Bancaria "+str(self._cuentaBancaria)+"\nUsuario: "+self._nomUsuario+"\nContrasenia: "+self._contrasenia
    def getCuentaBancaria(self):
        return self._cuentaBancaria
    def getNomUsuario(self):
        return self._nomUsuario
    def getContrasenia(self):
        return self._contrasenia
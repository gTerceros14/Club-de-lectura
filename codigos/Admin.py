from codigos.Personas import *
class Admin(Personas):
    def __init__(self,nombre="",apellido="",ci="",usuarioAdmin="ADMIN",contraseniaAdmin="ADMIN"):
        super().__init__(nombre,apellido,ci)
        self._usuarioAdmin=usuarioAdmin
        self._contraseniaAdmin=contraseniaAdmin
    def getUsuarioAmdin(self):
        return self._usuarioAdmin
    def getContraseniaAdmin(self):
        return self._contraseniaAdmin
  
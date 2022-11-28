from Persona import *
class Admin(Persona):
    def __init__(self, nombrePersona, apellidoPersona, nombreUsuario, CI, contrasenia, edad, permisoAdmin):
        super().__init__(nombrePersona, apellidoPersona, nombreUsuario, CI, contrasenia, edad)
        self._permisoAdmin = permisoAdmin
    
    def __str__(self) -> str:
        return super().__str__() + '\nPermiso admin: ' + str(self._permisoAdmin)

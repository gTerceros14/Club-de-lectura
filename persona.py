class Persona:
    def __init__(self, nombrePersona, apellidoPersona, nombreUsuario, CI, contrasenia, edad):
        self._nombrePersona = nombrePersona
        self._apellidoPersona = apellidoPersona
        self._nombreUsuario = nombreUsuario
        self._CI = CI
        self._contrasenia = contrasenia
        self._edad = edad
    
    def __str__(self) -> str:
        return  'Nombre completo: ' + str(self._nombrePersona + ' ' + self._apellidoPersona) + '\nNombre usuario: ' + str(self._nombreUsuario) + '\nCI: ' + str(self._CI) + '\nContrasenia: ' + str('*' * len(self._contrasenia)) + '\nEdad: ' + str(self._edad)
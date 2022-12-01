class Personas:
    def __init__(self,nombre,apellido,ci):
        self._nombre=nombre
        self._apellido=apellido
        self._ci=ci
    def __str__(self):
        return "\nNombre: "+self._nombre+"\nApellido"+self._apellido+"\nCi: "+str(self._ci)
    def getNombre(self):
        return self._nombre
    def getApellido(self):
        return self._apellido
    def getCi(self):
        return self._ci
    def getGenero(self):
        return self._genero
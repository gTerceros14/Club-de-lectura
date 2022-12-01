class Libro:
    def __init__(self,idLibro,nombre,fechaPub,autor,editorial,categoria,precio):
        self.idLibro=idLibro
        self.nombre=nombre
        self.fechaPub=fechaPub
        self.autor=autor
        self.editorial=editorial
        self.categoria=categoria
        self.precio=precio
    def __str__(self):
        return "\nID libro"+self.idLibro+"\nNombre: "+self.nombre+"\fecha de publicacion: "+str(self.fechaPub)+"\nAutor: "+self.autor+"Editorial: "+self.editorial+"Categoria: "+self.categoria,"Precio: "+self.precio
    def getIDLibro(self):
        return self.idLibro
    def getNombre(self):
        return self.nombre
    def getFechaPub(self):
        return self.fechaPub
    def getEditorial(self):
        return self.editorial
    def getCategoria(self):
        return self.categoria
    def getPrecio(self):
        return self.precio
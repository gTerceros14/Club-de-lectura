class Libro:
    def __init__(self, ID, nombreLibro, autor, precio, categoria, editorial) -> None:
        self._idLibro = ID
        self._nombreLibro = nombreLibro
        self._autor = autor
        self._precio = precio
        self._categoria = categoria
        self._editorial = editorial

    def __str__(self) -> str:
        return 'Nombre libro: ' + str(self._nombreLibro) + '\nAutor: ' + str(self._autor) + '\nPrecio: ' + str(self._precio) + '\nCategoria: ' + str(self._categoria) + '\nEditorial: ' + str(self._editorial)

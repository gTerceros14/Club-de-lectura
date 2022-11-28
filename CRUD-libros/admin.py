from persona import *
from libros import *
import conexion as conn

class Admin(Persona):

    def __init__(self, nombre, apellido, nickname, password, CI, edad, permisoAdmin=True):
        super().__init__(nombre, apellido, nickname, password, CI, edad)
        self.permisoAdmin = permisoAdmin  
        self.database = conn.DB()
    
    def menuDatosLibros(self):
        try:
            nombre = input('Nombre: ')
            autor = input('Autor: ')
            precio = float(input('Precio: '))
            categoria = input('Categoria: ')
            editorial = input('Editorial: ')
            
            if len(nombre)>0 and len(autor)>0 and precio>0 and len(categoria)>0 and len(editorial)>0:
                libro = Libro(nombre, autor, precio, categoria, editorial)
                return libro
            else:
                return '-- No deje atributos en blanco --'
        except:
            return '-- Tipo de dato incorrecto --'

    def createLibrosSQL(self):
        print('='*30)
        print('\tRegistra un libro ...')
        retorno = self.menuDatosLibros()
        try:
            consultaSQL = 'INSERT INTO libros(nombre, autor, precio, categoria, editorial) VALUES (?,?,?,?,?)'
            parametros = (retorno.nombre, retorno.autor, retorno.precio, retorno.categoria, retorno.editorial)
            self.database.ejecutar_consulta(consultaSQL, parametros)
            print('Libro registrado con exito ...')
        except:
            print('-- No se registro nada --')

    def readLibrosSQL(self):
        try:
            consultaSQL = self.database.ejecutar_consulta('SELECT * FROM libros')
            for datos in consultaSQL:
                print(f"""
    ID: {datos[0]}
    Nombre: {datos[1]}
    Autor: {datos[2]}
    Precio: {datos[3]}
    Categoria: {datos[4]}
    Editorial: {datos[5]}""")
        except:
            print('-- Hubo un error al mostrar el registro --')
    
    def updateLibrosSQL(self):
        print('='*30)
        print('\tActuliza los datos ...')
        try:
            id = int(input('ID libro: '))
            if id > 0:
                retorno = self.menuDatosLibros()
                consultaSQL = 'UPDATE libros SET nombre=?, autor=?, precio=?, categoria=?, editorial=? WHERE ID_libro=?'
                parametros = (retorno.nombre, retorno.autor, retorno.precio, retorno.categoria, retorno.editorial, id)
                self.database.ejecutar_consulta(consultaSQL, parametros)
                print('\nRegistro actualizado ...')
            else    :
                print('-- ID invalido --')
        except:
            print('-- Hubo un error al actualizar el registro --')
    
    def deleteLibrosSQL(self):
        try:
            id = int(input('ID libro: '))
            if id > 0:
                consultaSQL = 'DELETE FROM libros WHERE ID_libro=?'
                parametros = (id,)
                self.database.ejecutar_consulta(consultaSQL, parametros)
                print('\nRegistro eliminado ...')
            else:
                print('-- ID invalido --')
        except:
            print('-- Hubo un error al eliminar el registro --')

    def searchLibrosSQL(self):
        try:
            nombre = input('Buscar: ')
            if len(nombre)>0:
                consultaSQL = 'SELECT * FROM libros WHERE nombre LIKE ?'
                parametros = (f'%{nombre}%',)
                retorno = self.database.ejecutar_consulta(consultaSQL, parametros)
                for datos in retorno:
                    print(f"""
    ID: {datos[0]}
    Nombre: {datos[1]}
    Autor: {datos[2]}
    Precio: {datos[3]}
    Categoria: {datos[4]}
    Editorial: {datos[5]}""")
        except:
            print('-- Hubo un error al buscar el registro --')
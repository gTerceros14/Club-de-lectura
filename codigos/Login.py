from codigos.Usuario import Usuario
from codigos.Libro import Libro
from codigos.Admin import Admin
from codigos.Conexion import Conexion
import codigos.conexionDB as conn
class Login:
    def __init__(self):
        self._conexion=Conexion()
        self._admin=Admin()
        self.db = conn.DB()

    

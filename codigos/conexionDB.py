import sqlite3
database="./BaseDatos/clubLiteratura.sqlite3"
class DB:
    def ejecutarConsulta(self,consulta,parametros=()):
        with sqlite3.connect(database) as conexionDB:
            self.cursor = conexionDB.cursor()
            result = self.cursor.execute(consulta,parametros)
            conexionDB.commit()
            return result




import sqlite3

database = 'database.db'

class DB:
    def ejecutar_consulta(self, consulta, parametros=()):
        with sqlite3.connect(database) as conectar:
            self.cursor = conectar.cursor()
            retorno = self.cursor.execute(consulta, parametros)
            conectar.commit()
            return retorno

#baseDeDatos = DB()
#resultado = baseDeDatos.ejecutar_consulta('SELECT * FROM libros')
#print(resultado.fetchall())
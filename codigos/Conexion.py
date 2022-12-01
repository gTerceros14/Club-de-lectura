import codigos.conexionDB as conn
class Conexion:
    def __init__(self):
        self.db = conn.DB()

    def Registro(self):
        try:
            print("Registrar Usuario")
            print("****************")
            nombre=str(input("Nombre: "))
            apellido=str(input("Apellido: "))
            ci=int(input("Ci: "))
            cuentaBancaria=int(input("Cuenta Bancaria: "))
            sql="SELECT * FROM banco WHERE numeroCuenta=?"
            parametros=(cuentaBancaria,)
            if self.db.ejecutarConsulta(sql,parametros).fetchall()==[]:
                print("No existe la cuenta bancaria")
                print("crear una cuenta")
                password=input("Password banco: ")
                saldo=float(input("Saldo: "))
                if saldo>=5:
                    sql="INSERT INTO banco (numeroCuenta,password,saldo) VALUES (?,?,?)"
                    parametros=(cuentaBancaria,password,saldo)
                    self.db.ejecutarConsulta(sql,parametros)
                    nomUsuario=str(input("Nombre de Usuario: "))
                    contrasenia=str(input("Contrasenia: "))
                    parametros=(nombre,apellido,ci,cuentaBancaria,nomUsuario,contrasenia,"Nuevo ingreso")
                    sql="INSERT INTO usuario(nombre,apellido,ci,cuentaBancaria,nomUsuario,contrasenia,estado) VALUES(?,?,?,?,?,?,?)"
                    self.db.ejecutarConsulta(sql,parametros)
                    print("Usuario insertado") 
                else:
                    print("No pudo registrarse, el saldo debe ser mayor a 5 bs")
                    self.Registro()
            else:
                nomUsuario=str(input("Nombre de Usuario: "))
                contrasenia=str(input("Contrasenia: "))
                parametros=(nombre,apellido,ci,cuentaBancaria,nomUsuario,contrasenia,"Nuevo ingreso")
                sql="INSERT INTO usuario(nombre,apellido,ci,cuentaBancaria,nomUsuario,contrasenia,estado) VALUES(?,?,?,?,?,?,?)"
                self.db.ejecutarConsulta(sql,parametros)
                print("Usuario insertado")   
        except:
            print("Error al registrar Usuario")
    def RegistroLibro(self):
        try:
            print("Registrar Libro")
            print("****************")
            nombre=str(input("Nombre del libro: "))
            fechaPub=input("Fecha de publicacion: ")
            autor=str(input("Autor: "))
            editorial=str(input("Editorial: "))
            categoria=str(input("categoria: "))
            precio=int(input("Precio"))
            calificacion=0
            parametros=(nombre,fechaPub,autor,editorial,categoria,precio,calificacion)
            sql="INSERT INTO libros(nombre,fechaPub,autor,editorial,categoria,precio,calificacion) VALUES(?,?,?,?,?,?,?)"
            self.db.ejecutarConsulta(sql,parametros)
            print("Libro insertado")
        except:
            print("error al registrar libro")

    def MostrarLibro(self):
        sql="SELECT * FROM libros"
        resultado=self.db.ejecutarConsulta(sql).fetchall()
        for i in range(len(resultado)):
            sql="SELECT reseñas.id_reseña, reseñas.reseña, reseñas.calificacionPos, reseñas.calificacionNeg FROM reseñas WHERE id_libro=?"
            parametros=(resultado[i][0],)
            resultadoResenia=self.db.ejecutarConsulta(sql,parametros).fetchall()
            print("Id libro", resultado[i][0])
            print("Nombre ", resultado[i][1])
            print("Autor ", resultado[i][2])
            print("Precio ", resultado[i][3])
            print("Categoria", resultado[i][4])
            print("Editorial", resultado[i][5])
            print("Fecha de publicacion", resultado[i][6])
            print("Calificacion :",resultado[i][7])
            print("")
            if resultadoResenia!=[]:
                for j in range(len(resultadoResenia)):
                    print("Id resenia ",resultadoResenia[j][0])
                    print("Resenia ",resultadoResenia[j][1])
                    print("Calificacion positiva ",resultadoResenia[j][2])
                    print("Calificacaion Negativa ",resultadoResenia[j][3])
                    print("")
            else:
                print(" sin reseña")
            print("="*25)
            print("")      
            
    def ActualizarLibro(self):
        try:
            id=int(input("ID libro: "))
            if self.buscarLibro(id)==True:
                nombre = input("Nombre: ")
                autor=input("Autor: ")
                precio=int(input("precio: "))
                categoria=input("Categoria: ")
                editorial=input("Editorial: ")
                fechaPub=input("Fecha de publicacion: ")
                sql="UPDATE libros SET nombre=?, autor=?, precio=?, categoria=?, editorial=?,fechaPub=? WHERE id_libro=?"
                parametros=(nombre,autor,precio,categoria,editorial,id,fechaPub)
                self.db.ejecutarConsulta(sql,parametros)
            else:
                print(" No existe libro")
        except:
            print(" error al actualizar libro" )
    


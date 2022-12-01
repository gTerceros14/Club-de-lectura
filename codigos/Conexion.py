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

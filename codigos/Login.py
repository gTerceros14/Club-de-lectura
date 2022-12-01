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


    def ingresar(self,dato):

        # FUNCIONES USUARIO
        if dato==1:
            if self._conexion.UsuariosExistentes():
                datos=self._conexion.VerificarContrasenia()
                if datos:
                    print("A ingresado al sistema del club de libros como CLIENTE: ",datos[0][1],datos[0][2])
                    if datos[0][7]=='Nuevo ingreso':
                        print("NUEVO INGRESO")
                        if self._conexion.actualizarSaldo(datos[0][4],5)==1:
                            print("Se le otorgo 5 libros de programacion como paquete de bienvenida")
                            sql="SELECT * FROM libros WHERE categoria=?"
                            parametros=("Programacion",)
                            resultado=self.db.ejecutarConsulta(sql,parametros).fetchall()
                            for i in range(len(resultado)):
                                sql="INSERT INTO ventas (id_usuario,id_libro,nombre,autor,precio,categoria,editorial,fechapub) VALUES (?,?,?,?,?,?,?,?)"
                                parametros=(datos[0][0],resultado[i][0],resultado[i][1],resultado[i][2],resultado[i][3],resultado[i][4],resultado[i][5],resultado[i][6])
                                self.db.ejecutarConsulta(sql,parametros)
                            sql="UPDATE usuario SET estado=? WHERE id_usuario=?"
                            parametros=("Usuario Regular",datos[0][0])
                            self.db.ejecutarConsulta(sql,parametros)
                        else:
                            print("La constrasenia de la cuenta bancaria es incorrecta")
                            self.ingresar(dato)
                    opcion=-1
                    while opcion!=0:
                        print("""
                        [1]Comprar libro
                        [2]Reseniar
                        [3]Calificar libro
                        [4]Calificar resenia
                        [5]Ver calificacion de libros y resenias
                        [6]ver libros comprados
                        [7]ver saldo
                        [8]recargar saldo
                        [0]Salir""")
                        try:              
                            opcion=int(input(">> "))
                        
                            if opcion==1:
                                self._conexion.MostrarLibro()
                                print("-"*35)
                                self._conexion.venderLibro(datos[0][0],datos[0][4])
                            if opcion==2:
                                self._conexion.reseniarLibro(datos[0][0])
                            if opcion==3:
                                self._conexion.calificarLibro(datos[0][0])
                            if opcion==4:
                                self._conexion.calificarResenia()
                            if opcion==5:
                                self._conexion.verCalificacionResenia()
                            if opcion==6:
                                self._conexion.librosComprados(datos[0][0])
                            if opcion==7:
                                self._conexion.verSaldo(datos[0][4])
                            if opcion==8:
                                self._conexion.recargarSaldo(datos[0][4])
                            elif opcion==0:
                                pass
                        except:
                            print("opcion invalida")
                else:
                    print("La contrasenia o usuario es incorrecta: ")
                    self.ingresar(dato)
            else:
                print("NO hay usuarios registrados")

        elif dato==2:
            usuarioAdmin=input("Ingrese usuario: ")
            contraseniaAdmin=input("Ingrese contrasenia: ")
            sql="SELECT * FROM administrador WHERE usuarioAdmin =? And contraseniaAdmin=?"
            parametros=(usuarioAdmin,contraseniaAdmin)
            resultado=self.db.ejecutarConsulta(sql,parametros)
            if resultado.fetchall():
                print("A ingresado al sistema del club de libros como ADMIN: ")
                opcion=-1
                while opcion!=0:
                    print("""
                    [1]Agregar libro
                    [2]Eliminar libro
                    [3]Actualizar contenido del libro
                    [4]Ver libros
                    [5]Ver usuarios registrados
                    [0]Salir""")
                    try:              
                        opcion=int(input(">> "))
                    
                        if opcion==1:
                            self._conexion.RegistroLibro()
                        if opcion==2:
                            self._conexion.EliminarLibro()
                        if opcion==3:
                            self._conexion.ActualizarLibro()
                        if opcion==4:
                            self._conexion.MostrarLibro()
                        if opcion==5:
                            self._conexion.MostrarUsuario()

                        elif opcion==0:
                            pass
                    except:
                        print("Opcion invalida")
            else:
                print("La contrasenia o usuario es incorrecta: ")
                self.ingresar(dato)
            

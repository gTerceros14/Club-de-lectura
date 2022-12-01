import conexionDB as conn
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
                parametros=(nombre,autor,precio,categoria,editorial,fechaPub,id)
                self.db.ejecutarConsulta(sql,parametros)
            else:
                print(" No existe libro")
        except:
            print(" error al actualizar libro" )
    def EliminarLibro(self):
        try:
            id=int(input("ID libro: "))
            if self.buscarLibro(id)==True:
                sql="DELETE FROM libros WHERE id_libro=?"
                parametros=(id,)
                self.db.ejecutarConsulta(sql,parametros)
            else:
                print("no existe libro")
        except:
            print("hubo un error ")	

    # GERMAN
    def verCalificacionResenia(self):
        self.MostrarLibro()
    
    def librosComprados(self,id):
        #sql="SELECT libros.nombre,libros.autor,libros.categoria,libros.editorial,libros.fechaPub,libros.calificacion from ventas,libros WHERE ventas.id_usuario=? and ventas.id_libro=libros.id_libro"
        sql="SELECT ventas.Nombre, ventas.autor, ventas.categoria, ventas.editorial, ventas.fechapub, ventas.precio from ventas WHERE id_usuario=? " 
        resultado=self.db.ejecutarConsulta(sql,(id,))
        datos=resultado.fetchall()
        for i in range(len(datos)):
            print("="*25)
            print("libro # : ",i+1)
            print("Nombre ", datos[i][0])
            print("Autor ", datos[i][1])
            print("Categoria", datos[i][2])
            print("Editorial", datos[i][3])
            print("Fecha de publicacion", datos[i][4])
            print("Precio :",datos[i][5])
            print("="*25)
    
    def verSaldo(self,cuentaBanco):
        sql="SELECT * FROM banco WHERE numeroCuenta=?"
        resultado=self.db.ejecutarConsulta(sql,(cuentaBanco,)).fetchall()
        print("="*25)
        print("Numero de cuenta: ",resultado[0][1])
        print("Saldo disponible: ",resultado[0][3])
        print("="*25)
        return resultado[0][3]
    
    #Edil 
    def buscarLibro(self,id):
        sql="SELECT * FROM libros WHERE id_libro=?"
        parametros=(id,)
        resultado=self.db.ejecutarConsulta(sql,parametros).fetchall()
        if resultado==[]:
            return False
        else: 
            return True
    def buscarResenia(self,id,resenia):
        sql="SELECT * FROM reseñas WHERE id_libro=? and id_reseña=?"
        parametros=(id,resenia)
        resultado=self.db.ejecutarConsulta(sql,parametros).fetchall()
        if resultado==[]:
            return False
        else:
            return True
    def UsuariosExistentes(self):
        sql="SELECT * FROM usuario"
        resultado=self.db.ejecutarConsulta(sql)
        datos=resultado.fetchall()
        return datos

    #Kelly

    def actualizarSaldo(self,cuentaBanco,monto):
        sql="SELECT * FROM banco WHERE numeroCuenta=?"
        parametros=(cuentaBanco,)
        resultado=self.db.ejecutarConsulta(sql,parametros).fetchall()
        password=input("ingrese password de banco: ")
        if password==resultado[0][2]:
            nuevoSaldo=resultado[0][3]-monto
            if nuevoSaldo==0:
                print("Saldo en 0 recargue porfavor")
            if nuevoSaldo<0:
                print("Necesita recargar Saldo insuficiente")
            sql="UPDATE banco SET saldo=? WHERE numeroCuenta=?"
            parametros=(nuevoSaldo,cuentaBanco)
            self.db.ejecutarConsulta(sql,parametros)
            return 1
        else:
            return 2
    def recargarSaldo(self,cuentaBanco):
        try:
            sql="SELECT * FROM banco WHERE numeroCuenta=?"
            resultado=self.db.ejecutarConsulta(sql,(cuentaBanco,)).fetchall()
            print("="*25)
            password=input("Password banco: ")
            if password==resultado[0][2]:
                recarga=float(input("ingrese monto a recargar: "))
                nuevoSaldo=recarga+resultado[0][3]
                sql="UPDATE banco SET saldo=? WHERE numeroCuenta=?"
                self.db.ejecutarConsulta(sql,(nuevoSaldo,cuentaBanco))
            else: 
                print("contraseña incorrecta")
            print("="*25)
        except:
            print("Error al recargar saldo")

    #valentin 
    def calificarLibro(self,usuario):
        try:
            self.MostrarLibro()
            id=int(input("ingrese el ID libro a calificar: "))
            if self.buscarLibro(id)==True:
                calificacion=int(input("Calificacion 0 - 10 :  "))
                if calificacion>=0 and calificacion <=10:
                    sql="INSERT INTO calificacion(id_usuario,id_libro,calificacion) VALUES(?,?,?)"
                    parametros=(usuario,id,calificacion)
                    self.db.ejecutarConsulta(sql,parametros)
                    sql="SELECT id_libro from libros"
                    resultado=self.db.ejecutarConsulta(sql).fetchall()
                    lista=[]
                    listaSuma=[]
                    for dato in resultado:
                        dato=list(dato)
                        lista=lista+dato
                    for id in lista:
                        suma=0
                        listaSuma.clear()
                        sql="SELECT calificacion.calificacion FROM calificacion WHERE id_libro=?"
                        parametros=(id,)
                        resultadoSuma=self.db.ejecutarConsulta(sql,parametros).fetchall()
                        if resultadoSuma!=[]:
                            for calificacion in resultadoSuma:
                                calificacion=list(calificacion)
                                listaSuma=listaSuma+calificacion
                            suma= sum(listaSuma)/len(listaSuma)
                            sql="UPDATE libros SET calificacion=? WHERE id_libro=?"
                            parametros=(suma,id)
                            self.db.ejecutarConsulta(sql,parametros)
                        else:
                            pass
                    print("calificacion completa")
                else:
                    print("Rango calificacion no valido")
            else:
                print("no existe el libro")
        except:
            print("Error al ingresar el id")
    
    def calificarResenia(self):
        self.verCalificacionResenia()
        try:
            idLibro=int(input("ingrese el id del libro"))
            if self.buscarLibro(idLibro):
                idResenia=int(input("Ingrese el id de la resenia a calificar "))
                if self.buscarResenia(idLibro,idResenia):
                    calificar=input("seleccione 'positivo' 'negativo'= ")
                    sql="SELECT reseñas.calificacionPos, reseñas.calificacionNeg FROM reseñas WHERE id_reseña=? and id_libro=?"
                    parametros=(idResenia,idLibro)
                    resultado=self.db.ejecutarConsulta(sql,parametros).fetchall()
                    if resultado!=[]:
                        if calificar=='positivo':
                            suma=resultado[0][0]+1
                            sql="UPDATE reseñas SET calificacionPos=? WHERE id_libro=? and id_reseña=?"
                            parametros=(suma,idLibro,idResenia)
                            self.db.ejecutarConsulta(sql,parametros)
                        elif calificar=='negativo':
                            suma=resultado[0][1]+1
                            sql="UPDATE reseñas SET calificacionNeg=? WHERE id_libro=? and id_reseña=?"
                            parametros=(suma,idLibro,idResenia)
                            self.db.ejecutarConsulta(sql,parametros)
                else:
                    print("no existe la reseña")
            else:
                print("no existe el libro")
        except:
            print("Error al calificar resenia ")

    def VerificarContrasenia(self):
        usuarioCliente=input("Ingrese usuario: ")
        contraseniaCliente=input("Ingrese contrasenia: ")
        sql="SELECT * FROM usuario WHERE nomUsuario =? And contrasenia=?"
        parametros=(usuarioCliente,contraseniaCliente)
        resultado=self.db.ejecutarConsulta(sql,parametros)
        datos=resultado.fetchall()
        return datos

    #Salomon
    def venderLibro(self,usuario,cuentaBanco):
        try:
            id=int(input("ingrese el ID libro a comprar: "))
            if self.buscarLibro(id)==True:
                sql="SELECT * FROM libros WHERE id_libro=?"
                parametros=(id,)
                resultado=self.db.ejecutarConsulta(sql,parametros).fetchall()
                resultadoUsuario=self.db.ejecutarConsulta("SELECT banco.saldo FROM banco WHERE numeroCuenta=?",(cuentaBanco,)).fetchall()
                if resultado[0][3]<=resultadoUsuario[0][0]:
                    if self.actualizarSaldo(cuentaBanco,resultado[0][3])==1:
                        sql="INSERT INTO ventas(id_usuario,id_libro,nombre,autor,precio,categoria,editorial,fechaPub) VALUES(?,?,?,?,?,?,?,?)"
                        parametros=(usuario,id,resultado[0][1],resultado[0][2],resultado[0][3],resultado[0][4],resultado[0][5],resultado[0][6])
                        self.db.ejecutarConsulta(sql,parametros)
                        print("libro comprado")
                    else:
                        print("Contrasenia de la cuenta bancaria incorrecta")
                else:
                    print("Saldo insuficiente")
            else:
                print("no existe el libro")
            print("-"*25)
        except:
            print("Error al ingresar el id")

    def reseniarLibro(self,usuario):
        try:
            self.MostrarLibro()
            id=int(input("ingrese el ID libro a reseñar: "))
            if self.buscarLibro(id)==True:
                texto=input("Reseña: ")
                sql="INSERT INTO reseñas(id_usuario,id_libro,reseña,calificacionPos,calificacionNeg) VALUES(?,?,?,?,?)"
                parametros=(usuario,id,texto,0,0)
                self.db.ejecutarConsulta(sql,parametros)
                print("reseña completa")
            else:
                print("no existe el libro")
        except:
            print("Error al ingresar el id")
    
    def MostrarUsuario(self):
        sql="SELECT * FROM usuario"
        resultado=self.db.ejecutarConsulta(sql)
        datos=resultado.fetchall()
        for i in range(len(datos)):
            print("ID usuario", datos[i][0])
            print("Nombre ", datos[i][1])
            print("Apellido", datos[i][2])
            print("CI ", datos[i][3])
            print("Cuenta Bancaria", datos[i][4])
            print("Nombre de usuario", datos[i][5])
            print("Estado ")
            print(" ")
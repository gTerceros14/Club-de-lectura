from codigos.Login import Login
from codigos.Conexion import Conexion
from codigos.Herramientas import Herramientas
class Principal:
    def __init__(self):
        self.login=Login()
        self.conexion=Conexion()
        self.herramientas=Herramientas()
    def iniciar(self):
        try:
            n=-1
            while n!=0:
                print("""   MENU    
                    [1]Registrarse  
                    [2]Ingresar   
                    [0]Salir
                    """)
                n=int(input("ingrese el un numero del menu: "))
                if n==1:
                    self.conexion.Registro()
                elif n==2:
                    self.login.ingresar(self.herramientas.IngresarComo())
                elif n==0:
                    input
        except:
            print("Opcion no Valida")
            self.iniciar()



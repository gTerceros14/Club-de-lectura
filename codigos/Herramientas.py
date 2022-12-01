from codigos.Conexion import Conexion
class Herramientas:
    def __init__(self):
        self.conexion=Conexion()
    def IngresarComo(self):
        opcion=-1
        while opcion!=0:
            print("""       INGRESAR COMO
            [1]CLIENTE
            [2]ADMINISTRADOR
            [0]Volver atras""")
            try:              
                opcion=int(input(">> "))
            except:
                print("ingrese un numero del menu")
                self.IngresarComo()
            return opcion


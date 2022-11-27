class ClubLiteratura:
    def __init__(self, nombre, usuariosRegistrados, usuariosMensualidadActiva=None, usuariosMensualidadInactiva=None):
        self.nombre = nombre
        self.usuariosregistrados = usuariosRegistrados
        self.usuariosMensualidadActiva = usuariosMensualidadActiva
        self.usuariosMensualidadInactiva = usuariosMensualidadInactiva
    
    def menu():
        print('='*25)
        print('1. Registrar cliente')
        print('2. Ver promedio edad')
        print('3. Ver total recaudado')
        print('0. Salir')
        print('='*25)

    def menuSeleccion(self):
        while True:
            self.menu()
            opcion = input('-> ')
            if opcion == '1':
                pass
            elif opcion == '2':
                pass
            elif opcion == '3':
                pass
            elif opcion == '0':
                pass
                break
            else:
                print('-- opcion incorrecta --')

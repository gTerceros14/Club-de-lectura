from admin import *
import time
from os import system

class ClubLiteratura:

    def verificacionAdmin(self, admin):
        if admin.permisoAdmin == True:
            system('cls')
            print(f'\nUsuario administrador: {admin.nickname} ...')
            return True
        else:
            False

    def menuAdmin(self):
        print('='*30)
        print('Menu registro de libros')
        print('[1] Insertar libro')
        print('[2] Listar libros')
        print('[3] Actualizar libro')
        print('[4] Eliminar libro')
        print('[5] Buscar libro')
        print('[0] Salir')
        print('='*30)
    
    def opcionesMenuAdmin(self, admin):
        if self.verificacionAdmin(admin):
            while True:
                self.menuAdmin()
                try:
                    opcion = int(input('->: '))
                    if (opcion == 1):
                        admin.createLibrosSQL()
                        time.sleep(2)
                        system('cls')

                    elif (opcion == 2):
                        admin.readLibrosSQL()
                        time.sleep(1)

                    elif (opcion == 3):
                        admin.updateLibrosSQL()
                        time.sleep(2)
                        system('cls')

                    elif (opcion == 4):
                        admin.deleteLibrosSQL()
                        time.sleep(2)
                        system('cls')
                    
                    elif (opcion == 5):
                        admin.searchLibrosSQL()
                    
                    elif (opcion == 0):
                        break
                except:
                    print('-- Opcion incorrecta --')
                    time.sleep(2)
                    system('cls')
        else:
            print('-- Administrador sin permisos --')

    def registroUsuario(self):
        system('cls')
        try:
            nombre = input('Nombre: ')
            apellido = input('Apellido: ')
            nickname = input('Nickname: ')
            password = input('Password: ')
            CI = int(input('CI: '))
            edad = int(input('Edad: '))

            if nickname == 'vale' and password == '123':
                admin = Admin(nombre, apellido, nickname, password, CI, edad)
                self.opcionesMenuAdmin(admin)
            else:
                pass
                # Crear clase Usuario (no voy a hacer todo yo)
                #usuario = Usuario(nombre, apellido, nickname, password, CI, edad)
        except:
           print('-- Tipo de dato incorrecto --')
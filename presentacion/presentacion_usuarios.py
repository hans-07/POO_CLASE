from prettytable import PrettyTable
import maskpass
import bcrypt

import re

from auxiliares.auxiliar import nombre_app,version_app
from datos.modelos.usuario import Usuario
from negocio.negocio_usuarios import cargar_usuarios,crear_usuario
from negocio.negocio_paises import buscar_pais
from datos.repositorio.repositorio_usuarios import usuario_por_correo
from presentacion.menu import menu_principal
from auxiliares.validaciones import validar_rut, validar_correo, validar_contrasenia_segura, validar_genero

def mostrar_usuarios():
    tabla_usuarios = PrettyTable()
    tabla_usuarios = cargar_usuarios(tabla_usuarios)
    print(tabla_usuarios)

def datos_usuario():
    rut = nombre = apellido = correo = nombre_pais = fecha_nacimiento = genero = contrasenia = ''
    print('\nIngrese Datos Usuario')

    while rut == '':
        rut = input('RUT (12.345.678-5): ')
        if not validar_rut(rut):
            print('Rut NO VÁLIDO, ingrese nuevamente...')
            rut = ''

    while nombre == '':
        nombre = input('Nombre: ')

    while apellido == '':
        apellido = input('Apellido: ')

    while correo == '':
        correo = input('Correo: ')
        if not validar_correo(correo):
            print('Correo electrónico NO corresponde, ingrese nuevamente...')
            correo = ''

    nombre_pais = input('Nombre País: ')
    tabla_paises = PrettyTable()
    tabla_paises = buscar_pais(tabla_paises, nombre_pais)
    print(tabla_paises)
    id_pais = input('Id País: ')

    fecha_nacimiento = input('Fecha Nacimiento (dd/MM/aaaa): ')

    while genero == '':
        print('Opciones de Género')
        print('[1] Masculino')
        print('[2] Femenino')
        print('[3] Otro')
        genero = input('Opción Género [1-3]: ')
        if not validar_genero(genero):
            print('Género NO corresponde, ingrese nuevamente...')
            genero = ''

    while contrasenia == '':
        print('Ingrese una contraseña segura:')
        print('Al menos una minúscula\nAl menos una mayúscula\nAl menos un dígito\nAl menos un caracter especial')
        print('Al menos 8 caracteres de largo')
        contrasenia = maskpass.askpass(prompt="Contraseña: ", mask="*")
        if not validar_contrasenia_segura(contrasenia):
            print('Su contraseña NO es segura, ingrese nuevamente...')
            contrasenia = ''
        else:
            hashed = bcrypt.hashpw(contrasenia.encode(), bcrypt.gensalt())

    crear_usuario(rut, nombre.title(), apellido.title(), correo, id_pais, fecha_nacimiento, genero, hashed)
    
def login_usuario():
    while True:
        print(f'\n{nombre_app} {version_app}')
        print('='*len(nombre_app) + "=" + '='*len(version_app))
        print('\nIngrese los datos de\nInicio de Sesión')
        
        correo = ''
        while correo == '':
            correo = input('Correo: ')
            if not validar_correo(correo):
                print('Correo electrónico NO corresponde, ingrese nuevamente...')
                correo = ''
            else:
                usuario = usuario_por_correo(correo)
                if usuario:
                    contrasenia = input('Contraseña: ')
                    
                    if bcrypt.checkpw(contrasenia.encode(), usuario.password):
                        print("¡Contraseña Correcta!")
                        menu_principal()
                    else:
                        print("Contraseña incorrecta,\n ingrese nuevamente...")
                else:
                    print('Usuario no registrado.\n¿Desea registrarse?')
                    opcion_registro = input('Ingrese Si/No [s-n]: ')
                    
                    match opcion_registro.lower():
                        case 's':
                            datos_usuario()
                        case 'n':
                            break
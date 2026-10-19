import sys

from datos import main_menu, nombre_app, version_app
from presentacion.menu_almacenes import menu_almacenes
from presentacion.menu_productos import menu_productos
from presentacion.menu_proveedores import menu_proveedores


def menu_principal():
    print(f'\n{nombre_app} - {version_app}')
    print('=' * len(nombre_app))

    while True:
        print('\n=== MENÚ PRINCIPAL ===')
        for clave, valor in main_menu.items():
            print(f'[{clave}] {valor}')

        opcion_usuario = input('\nSeleccione una opción [1-4]: ')

        if opcion_usuario == '1':
            menu_productos()
        elif opcion_usuario == '2':
            menu_almacenes()
        elif opcion_usuario == '3':
            menu_proveedores()
        elif opcion_usuario == '4':
            print('\nSaliendo del sistema...')
            sys.exit()
        else:
            print('\nOpción inválida. Intente nuevamente.')
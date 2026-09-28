import sys
from datos import nombre_app, version_app, main_menu

def menu_principal():
    print(f'{nombre_app} - {version_app}')
    print('='*len(nombre_app) + '='*len(version_app))

while True:
    for (clave, valor) in main_menu.items():
        print(f'[{clave}] {valor}')

    opcion_usuario = input('Seleccione una opción [1-4]: ')

    if opcion_usuario == '1':
        print('Gestionar Productos')
    elif opcion_usuario == '2':
        print('Gestionar Clientes')
    elif opcion_usuario == '3':
        print('Gestionar Proveedores')
    elif opcion_usuario == '4':
        print('Saliendo del programa...')
        sys.exit()
    else:
        print('Opción inválida. Por favor, seleccione una opción válida.')
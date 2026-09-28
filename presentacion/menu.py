import sys
from datos import nombre_app, version_app

def menu_principal():
    print(f'{nombre_app} - {version_app}')
    print('='*len(nombre_app) + '='*len(version_app))

while True:
    print('[1] Gestionar Productos')
    print('[2] Gestionar Clientes')
    print('[3] Gestionar Proveedores')
    print('[4] Salir')
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
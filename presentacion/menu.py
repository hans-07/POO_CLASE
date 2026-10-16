import sys

from datos import main_menu, nombre_app, version_app
from negocio.negocio_productos import crear_producto_demo, obtener_productos
from presentacion.menu_almacenes import mostrar_almacenes
from presentacion.menu_productos import mostrar_productos
from presentacion.menu_proveedores import mostrar_proveedores


def menu_principal():
    print(f'\n{nombre_app} - {version_app}')
    print('=' * len(nombre_app))

    while True:
        print('\n=== MENÚ PRINCIPAL ===')
        for clave, valor in main_menu.items():
            print(f'[{clave}] {valor}')

        opcion_usuario = input('\nSeleccione una opción [1-5]: ')

        if opcion_usuario == '1':
            mostrar_productos()
        elif opcion_usuario == '2':
            mostrar_almacenes()
        elif opcion_usuario == '3':
            mostrar_proveedores()
        elif opcion_usuario == '4':
            print('\nCargando datos demo...')
            crear_producto_demo()
            print('Datos demo insertados correctamente.')
            print('Productos actuales:')
            for producto in obtener_productos():
                print(f'- {producto.id_producto}: {producto.nombre} | ${producto.precio_venta}')
        elif opcion_usuario == '5':
            print('\nSaliendo del sistema...')
            sys.exit()
        else:
            print('\nOpción inválida. Intente nuevamente.')
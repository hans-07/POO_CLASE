from prettytable import PrettyTable

from negocio.negocio_almacenes import (
    borrar_almacen,
    buscar_almacen_por_id,
    crear_almacen,
    editar_almacen,
    obtener_almacenes,
)


def _mostrar_tabla_almacenes(almacenes):
    tabla = PrettyTable()
    tabla.field_names = ['ID', 'Nombre', 'Dirección', 'Estado']
    for almacen in almacenes:
        tabla.add_row([
            almacen.id_almacen,
            almacen.nombre_almacen,
            almacen.direccion,
            'Activo' if almacen.estado else 'Inactivo',
        ])
    print(tabla)


def mostrar_almacenes():
    almacenes = obtener_almacenes()
    print('\n--- Almacenes ---')
    if not almacenes:
        print('No hay almacenes registrados.')
        return

    _mostrar_tabla_almacenes(almacenes)


def menu_almacenes():
    while True:
        print('\n=== GESTIÓN DE ALMACENES ===')
        print('[1] Listar almacenes')
        print('[2] Crear almacén')
        print('[3] Actualizar almacén')
        print('[4] Eliminar almacén')
        print('[5] Volver')

        opcion = input('\nSeleccione una opción [1-5]: ')

        if opcion == '1':
            mostrar_almacenes()
        elif opcion == '2':
            try:
                nombre = input('Nombre del almacén: ').strip()
                direccion = input('Dirección: ').strip()
                estado = input('Estado activo? (s/n): ').strip().lower() == 's'
                almacen = crear_almacen(nombre, direccion, estado)
                print(f'Almacén creado correctamente: {almacen.id_almacen}')
            except ValueError as error:
                print(f'Error: {error}')
        elif opcion == '3':
            try:
                almacen_id = int(input('ID del almacén a actualizar: ').strip())
                almacen = buscar_almacen_por_id(almacen_id)
                if almacen is None:
                    print('Almacén no encontrado.')
                    continue

                nombre = input(f'Nuevo nombre [{almacen.nombre_almacen}]: ').strip() or almacen.nombre_almacen
                direccion = input(f'Nueva dirección [{almacen.direccion}]: ').strip() or almacen.direccion
                estado_input = input(f'Estado activo? [{"s" if almacen.estado else "n"}]: ').strip().lower()
                estado = almacen.estado if estado_input == '' else estado_input == 's'

                almacen_actualizado = editar_almacen(almacen_id, nombre, direccion, estado)
                print(f'Almacén actualizado correctamente: {almacen_actualizado.id_almacen}')
            except ValueError:
                print('Debe ingresar valores válidos.')
        elif opcion == '4':
            try:
                almacen_id = int(input('ID del almacén a eliminar: ').strip())
                almacen = buscar_almacen_por_id(almacen_id)
                if almacen is None:
                    print('Almacén no encontrado.')
                    continue

                confirmado = input(f'¿Desea eliminar el almacén {almacen.nombre_almacen}? (s/n): ').strip().lower()
                if confirmado != 's':
                    print('Eliminación cancelada.')
                    continue

                if borrar_almacen(almacen_id):
                    print('Almacén eliminado correctamente.')
                else:
                    print('No se pudo eliminar el almacén.')
            except ValueError:
                print('Debe ingresar un ID válido.')
        elif opcion == '5':
            return
        else:
            print('Opción inválida.')

from prettytable import PrettyTable

from negocio.negocio_proveedores import (
    borrar_proveedor,
    buscar_proveedor_por_id,
    buscar_proveedor_por_rut,
    crear_proveedor,
    editar_proveedor,
    obtener_proveedores,
)


def _mostrar_tabla_proveedores(proveedores):
    tabla = PrettyTable()
    tabla.field_names = ['ID', 'RUT', 'Razón Social', 'Teléfono', 'Email']
    for proveedor in proveedores:
        tabla.add_row([
            proveedor.id_proveedor,
            proveedor.rut_proveedor,
            proveedor.razon_social,
            proveedor.telefono or '-',
            proveedor.email or '-',
        ])
    print(tabla)


def mostrar_proveedores():
    proveedores = obtener_proveedores()
    print('\n--- Proveedores ---')
    if not proveedores:
        print('No hay proveedores registrados.')
        return

    _mostrar_tabla_proveedores(proveedores)


def menu_proveedores():
    while True:
        print('\n=== GESTIÓN DE PROVEEDORES ===')
        print('[1] Listar proveedores')
        print('[2] Crear proveedor')
        print('[3] Actualizar proveedor')
        print('[4] Eliminar proveedor')
        print('[5] Volver')

        opcion = input('\nSeleccione una opción [1-5]: ')

        if opcion == '1':
            mostrar_proveedores()
        elif opcion == '2':
            try:
                rut = input('RUT: ').strip()
                razon_social = input('Razón social: ').strip()
                telefono = input('Teléfono: ').strip()
                email = input('Email: ').strip()

                proveedor = crear_proveedor(rut, razon_social, telefono or None, email or None)
                print(f'Proveedor creado correctamente: {proveedor.id_proveedor}')
            except ValueError as error:
                print(f'Error: {error}')
        elif opcion == '3':
            try:
                proveedor_id = int(input('ID del proveedor a actualizar: ').strip())
                proveedor = buscar_proveedor_por_id(proveedor_id)
                if proveedor is None:
                    print('Proveedor no encontrado.')
                    continue

                rut = input(f'Nuevo RUT [{proveedor.rut_proveedor}]: ').strip() or proveedor.rut_proveedor
                razon_social = input(f'Nueva razón social [{proveedor.razon_social}]: ').strip() or proveedor.razon_social
                telefono = input(f'Nuevo teléfono [{proveedor.telefono or "-"}]: ').strip() or proveedor.telefono
                email = input(f'Nuevo email [{proveedor.email or "-"}]: ').strip() or proveedor.email

                proveedor_actualizado = editar_proveedor(
                    proveedor_id,
                    rut_proveedor=rut,
                    razon_social=razon_social,
                    telefono=telefono,
                    email=email,
                )
                print(f'Proveedor actualizado correctamente: {proveedor_actualizado.id_proveedor}')
            except ValueError:
                print('Debe ingresar valores válidos.')
        elif opcion == '4':
            try:
                proveedor_id = int(input('ID del proveedor a eliminar: ').strip())
                proveedor = buscar_proveedor_por_id(proveedor_id)
                if proveedor is None:
                    print('Proveedor no encontrado.')
                    continue

                confirmado = input(f'¿Desea eliminar el proveedor {proveedor.razon_social}? (s/n): ').strip().lower()
                if confirmado != 's':
                    print('Eliminación cancelada.')
                    continue

                if borrar_proveedor(proveedor_id):
                    print('Proveedor eliminado correctamente.')
                else:
                    print('No se pudo eliminar el proveedor.')
            except ValueError:
                print('Debe ingresar un ID válido.')
        elif opcion == '5':
            return
        else:
            print('Opción inválida.')

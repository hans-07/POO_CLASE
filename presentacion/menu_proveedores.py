from negocio.negocio_proveedores import obtener_proveedores


def mostrar_proveedores():
    proveedores = obtener_proveedores()
    print('\n--- Proveedores ---')
    if not proveedores:
        print('No hay proveedores registrados.')
        return

    for proveedor in proveedores:
        print(f'ID: {proveedor.id_proveedor} | RUT: {proveedor.rut_proveedor} | Razón social: {proveedor.razon_social}')

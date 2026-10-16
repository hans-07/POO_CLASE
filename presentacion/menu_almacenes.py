from negocio.negocio_almacenes import obtener_almacenes


def mostrar_almacenes():
    almacenes = obtener_almacenes()
    print('\n--- Almacenes ---')
    if not almacenes:
        print('No hay almacenes registrados.')
        return

    for almacen in almacenes:
        print(f'ID: {almacen.id_almacen} | Nombre: {almacen.nombre_almacen} | Dirección: {almacen.direccion}')

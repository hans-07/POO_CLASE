from negocio.negocio_productos import obtener_productos


def mostrar_productos():
    productos = obtener_productos()
    print('\n--- Productos ---')
    if not productos:
        print('No hay productos registrados.')
        return

    for producto in productos:
        print(f'ID: {producto.id_producto} | Nombre: {producto.nombre} | Precio: {producto.precio_venta}')

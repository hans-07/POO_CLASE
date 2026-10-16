from datos.repositorio.repositorio_productos import guardar_producto, listar_productos


def crear_producto(nombre, descripcion, precio_venta, categoria, proveedor_principal):
    from datos.modelos.producto import Producto

    producto = Producto(
        nombre=nombre,
        descripcion=descripcion,
        precio_venta=precio_venta,
        categoria=categoria,
        proveedor_principal=proveedor_principal,
    )
    return guardar_producto(producto)


def obtener_productos():
    return listar_productos()

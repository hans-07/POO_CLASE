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


def crear_producto_demo():
    from datos.modelos.producto import Producto

    producto = Producto.get_or_create(
        nombre='Agua Mineral 1L',
        defaults={
            'descripcion': 'Botella de agua mineral sin gas',
            'precio_venta': 1200,
            'categoria': 1,
            'proveedor_principal': 1,
        }
    )
    return producto

from decimal import Decimal

from datos.repositorio.repositorio_productos import (
    actualizar_producto,
    eliminar_producto,
    guardar_producto,
    listar_productos,
    producto_por_id,
)


def crear_producto(nombre, descripcion, precio_venta, categoria, proveedor_principal):
    from datos.modelos.producto import Producto

    if not nombre or not nombre.strip():
        raise ValueError('El nombre del producto es obligatorio.')

    if precio_venta is None:
        raise ValueError('El precio de venta es obligatorio.')

    producto = Producto(
        nombre=nombre.strip(),
        descripcion=descripcion.strip() if descripcion else None,
        precio_venta=Decimal(str(precio_venta)),
        categoria=categoria,
        proveedor_principal=proveedor_principal,
    )
    return guardar_producto(producto)


def obtener_productos():
    return listar_productos()


def buscar_producto_por_id(id_producto):
    return producto_por_id(id_producto)


def editar_producto(id_producto, nombre=None, descripcion=None, precio_venta=None,
                   categoria=None, proveedor_principal=None):
    return actualizar_producto(
        id_producto=id_producto,
        nombre=nombre.strip() if nombre is not None else None,
        descripcion=descripcion.strip() if descripcion is not None else None,
        precio_venta=precio_venta,
        categoria=categoria,
        proveedor_principal=proveedor_principal,
    )


def borrar_producto(id_producto):
    return eliminar_producto(id_producto)



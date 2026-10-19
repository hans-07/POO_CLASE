from decimal import Decimal

from datos.modelos.producto import Producto


def guardar_producto(producto: Producto):
    return producto.save()


def listar_productos():
    return list(Producto.select().order_by(Producto.id_producto.asc()))


def producto_por_id(id_producto):
    return Producto.get_or_none(Producto.id_producto == id_producto)


def actualizar_producto(id_producto, nombre=None, descripcion=None, precio_venta=None,
                       categoria=None, proveedor_principal=None):
    producto = producto_por_id(id_producto)
    if producto is None:
        return None

    if nombre is not None:
        producto.nombre = nombre
    if descripcion is not None:
        producto.descripcion = descripcion
    if precio_venta is not None:
        producto.precio_venta = Decimal(str(precio_venta))
    if categoria is not None:
        producto.categoria = categoria
    if proveedor_principal is not None:
        producto.proveedor_principal = proveedor_principal

    producto.save()
    return producto


def eliminar_producto(id_producto):
    producto = producto_por_id(id_producto)
    if producto is None:
        return False

    return producto.delete_instance() > 0

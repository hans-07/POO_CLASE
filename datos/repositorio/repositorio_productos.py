from datos.modelos.producto import Producto


def guardar_producto(producto: Producto):
    return producto.save()


def listar_productos():
    return list(Producto.select())


def producto_por_id(id_producto):
    return Producto.get_or_none(Producto.id_producto == id_producto)

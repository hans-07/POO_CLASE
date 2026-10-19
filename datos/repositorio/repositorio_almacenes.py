from datos.modelos.almacen import Almacen


def guardar_almacen(almacen: Almacen):
    return almacen.save()


def listar_almacenes():
    return list(Almacen.select().order_by(Almacen.id_almacen.asc()))


def almacen_por_id(id_almacen):
    return Almacen.get_or_none(Almacen.id_almacen == id_almacen)


def actualizar_almacen(id_almacen, nombre_almacen=None, direccion=None, estado=None):
    almacen = almacen_por_id(id_almacen)
    if almacen is None:
        return None

    if nombre_almacen is not None:
        almacen.nombre_almacen = nombre_almacen
    if direccion is not None:
        almacen.direccion = direccion
    if estado is not None:
        almacen.estado = estado

    almacen.save()
    return almacen


def eliminar_almacen(id_almacen):
    almacen = almacen_por_id(id_almacen)
    if almacen is None:
        return False

    return almacen.delete_instance() > 0

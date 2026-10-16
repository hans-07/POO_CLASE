from datos.modelos.almacen import Almacen


def guardar_almacen(almacen: Almacen):
    return almacen.save()


def listar_almacenes():
    return list(Almacen.select())


def almacen_por_id(id_almacen):
    return Almacen.get_or_none(Almacen.id_almacen == id_almacen)

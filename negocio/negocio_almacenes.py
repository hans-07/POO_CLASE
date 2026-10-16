from datos.repositorio.repositorio_almacenes import guardar_almacen, listar_almacenes


def crear_almacen(nombre_almacen, direccion, estado=True):
    from datos.modelos.almacen import Almacen

    almacen = Almacen(
        nombre_almacen=nombre_almacen,
        direccion=direccion,
        estado=estado,
    )
    return guardar_almacen(almacen)


def obtener_almacenes():
    return listar_almacenes()

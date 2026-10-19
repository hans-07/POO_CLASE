from datos.repositorio.repositorio_almacenes import (
    actualizar_almacen,
    eliminar_almacen,
    listar_almacenes,
    almacen_por_id,
    guardar_almacen,
)


def crear_almacen(nombre_almacen, direccion, estado=True):
    from datos.modelos.almacen import Almacen

    if not nombre_almacen or not nombre_almacen.strip():
        raise ValueError('El nombre del almacén es obligatorio.')
    if not direccion or not direccion.strip():
        raise ValueError('La dirección del almacén es obligatoria.')

    almacen = Almacen(
        nombre_almacen=nombre_almacen.strip(),
        direccion=direccion.strip(),
        estado=estado,
    )
    return guardar_almacen(almacen)


def obtener_almacenes():
    return listar_almacenes()


def buscar_almacen_por_id(id_almacen):
    return almacen_por_id(id_almacen)


def editar_almacen(id_almacen, nombre_almacen=None, direccion=None, estado=None):
    return actualizar_almacen(
        id_almacen=id_almacen,
        nombre_almacen=nombre_almacen.strip() if nombre_almacen is not None else None,
        direccion=direccion.strip() if direccion is not None else None,
        estado=estado,
    )


def borrar_almacen(id_almacen):
    return eliminar_almacen(id_almacen)

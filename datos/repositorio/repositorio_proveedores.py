from datos.modelos.proveedor import Proveedor


def guardar_proveedor(proveedor: Proveedor):
    return proveedor.save()


def listar_proveedores():
    return list(Proveedor.select().order_by(Proveedor.id_proveedor.asc()))


def proveedor_por_id(id_proveedor):
    return Proveedor.get_or_none(Proveedor.id_proveedor == id_proveedor)


def proveedor_por_rut(rut_proveedor):
    return Proveedor.get_or_none(Proveedor.rut_proveedor == rut_proveedor)


def actualizar_proveedor(id_proveedor, rut_proveedor=None, razon_social=None,
                       telefono=None, email=None):
    proveedor = proveedor_por_id(id_proveedor)
    if proveedor is None:
        return None

    if rut_proveedor is not None:
        proveedor.rut_proveedor = rut_proveedor
    if razon_social is not None:
        proveedor.razon_social = razon_social
    if telefono is not None:
        proveedor.telefono = telefono
    if email is not None:
        proveedor.email = email

    proveedor.save()
    return proveedor


def eliminar_proveedor(id_proveedor):
    proveedor = proveedor_por_id(id_proveedor)
    if proveedor is None:
        return False

    return proveedor.delete_instance() > 0

from datos.modelos.proveedor import Proveedor


def guardar_proveedor(proveedor: Proveedor):
    return proveedor.save()


def listar_proveedores():
    return list(Proveedor.select())


def proveedor_por_rut(rut_proveedor):
    return Proveedor.get_or_none(Proveedor.rut_proveedor == rut_proveedor)

from datos.repositorio.repositorio_proveedores import guardar_proveedor, listar_proveedores


def crear_proveedor(rut_proveedor, razon_social, telefono=None, email=None):
    from datos.modelos.proveedor import Proveedor

    proveedor = Proveedor(
        rut_proveedor=rut_proveedor,
        razon_social=razon_social,
        telefono=telefono,
        email=email,
    )
    return guardar_proveedor(proveedor)


def obtener_proveedores():
    return listar_proveedores()

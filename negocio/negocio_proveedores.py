from datos.repositorio.repositorio_proveedores import (
    actualizar_proveedor,
    eliminar_proveedor,
    listar_proveedores,
    proveedor_por_id,
    proveedor_por_rut,
    guardar_proveedor,
)


def crear_proveedor(rut_proveedor, razon_social, telefono=None, email=None):
    from datos.modelos.proveedor import Proveedor

    if not rut_proveedor or not rut_proveedor.strip():
        raise ValueError('El RUT del proveedor es obligatorio.')
    if not razon_social or not razon_social.strip():
        raise ValueError('La razón social es obligatoria.')

    proveedor = Proveedor(
        rut_proveedor=rut_proveedor.strip(),
        razon_social=razon_social.strip(),
        telefono=telefono.strip() if telefono else None,
        email=email.strip() if email else None,
    )
    return guardar_proveedor(proveedor)


def obtener_proveedores():
    return listar_proveedores()


def buscar_proveedor_por_id(id_proveedor):
    return proveedor_por_id(id_proveedor)


def buscar_proveedor_por_rut(rut_proveedor):
    return proveedor_por_rut(rut_proveedor)


def editar_proveedor(id_proveedor, rut_proveedor=None, razon_social=None,
                    telefono=None, email=None):
    return actualizar_proveedor(
        id_proveedor=id_proveedor,
        rut_proveedor=rut_proveedor.strip() if rut_proveedor is not None else None,
        razon_social=razon_social.strip() if razon_social is not None else None,
        telefono=telefono.strip() if telefono is not None else None,
        email=email.strip() if email is not None else None,
    )


def borrar_proveedor(id_proveedor):
    return eliminar_proveedor(id_proveedor)

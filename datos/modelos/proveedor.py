from peewee import AutoField, CharField

from datos.models import BaseModel


class Proveedor(BaseModel):
    id_proveedor = AutoField()
    rut_proveedor = CharField(max_length=12, unique=True)
    razon_social = CharField()
    telefono = CharField(max_length=20, null=True)
    email = CharField(null=True)

    class Meta:
        table_name = 'proveedores'

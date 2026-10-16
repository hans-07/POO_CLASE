from datos.models import BaseModel
from peewee import AutoField, CharField, DecimalField, IntegerField, TextField


class Producto(BaseModel):
    id_producto = AutoField()
    nombre = CharField()
    descripcion = TextField(null=True)
    precio_venta = DecimalField(decimal_places=2, max_digits=10, default=0.00)
    categoria = IntegerField(index=True)
    proveedor_principal = IntegerField(index=True)

    class Meta:
        table_name = 'productos'

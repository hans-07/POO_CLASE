from peewee import AutoField, BooleanField, CharField

from datos.models import BaseModel


class Almacen(BaseModel):
    id_almacen = AutoField()
    nombre_almacen = CharField()
    direccion = CharField()
    estado = BooleanField(default=True)

    class Meta:
        table_name = 'almacenes'

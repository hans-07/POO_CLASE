from datos.conexion import BaseModel
from peewee import AutoField, BooleanField, CharField, DateTimeField, DecimalField



class Almacenes(BaseModel):
    direccion = CharField()
    estado = BooleanField(constraints=[SQL("DEFAULT 1")])
    id_almacen = AutoField()
    nombre_almacen = CharField()

    class Meta:
        table_name = 'almacenes'

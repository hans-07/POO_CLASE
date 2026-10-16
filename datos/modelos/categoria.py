from datos.models import BaseModel
from peewee import AutoField, CharField, TextField


class Categoria(BaseModel):
    id_categoria = AutoField()
    nombre_categoria = CharField(max_length=100)
    descripcion = TextField(null=True)

    class Meta:
        table_name = 'categorias'

from datetime import datetime

from peewee import AutoField, CharField, DateTimeField, DecimalField, IntegerField, TextField

from datos.models import BaseModel


class Entrada(BaseModel):
    id_entrada = AutoField()
    id_movimiento = IntegerField(index=True)
    fecha_hora = DateTimeField(default=datetime.now)
    numero_factura = CharField(max_length=50)
    costo_total = DecimalField(decimal_places=2, max_digits=12, default=0.00)
    observacion = TextField(null=True)

    class Meta:
        table_name = 'entradas'

    def registrar_entrada(self):
        return self.save()

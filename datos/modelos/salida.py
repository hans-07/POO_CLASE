from datetime import datetime

from peewee import AutoField, CharField, DateTimeField, DecimalField, IntegerField

from datos.models import BaseModel


class Salida(BaseModel):
    id_salida = AutoField()
    id_movimiento = IntegerField(index=True)
    fecha_hora = DateTimeField(default=datetime.now)
    motivo = CharField()
    monto_total = DecimalField(decimal_places=2, max_digits=12, default=0.00)
    estado_salida = CharField(max_length=20, default='pendiente')

    class Meta:
        table_name = 'salidas'

    def registrar_salida(self):
        return self.save()

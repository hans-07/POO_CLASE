from datetime import datetime

from peewee import AutoField, CharField, DateTimeField, DecimalField, IntegerField

from datos.models import BaseModel


class DetalleMovimiento(BaseModel):
    id_movimiento = AutoField()
    id_ubicacion = IntegerField(index=True)
    fecha_hora = DateTimeField(default=datetime.now)
    tipo_movimiento = CharField(max_length=20)
    motivo = CharField(null=True)
    cantidad = IntegerField()
    costo_unitario = DecimalField(decimal_places=2, max_digits=10, default=0.00)

    class Meta:
        table_name = 'detalle_movimientos'

    def calcular_subtotal(self):
        return self.cantidad * self.costo_unitario

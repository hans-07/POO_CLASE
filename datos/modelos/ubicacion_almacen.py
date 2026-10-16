from peewee import AutoField, IntegerField

from datos.models import BaseModel


class UbicacionAlmacen(BaseModel):
    id_ubicacion = AutoField()
    id_almacen = IntegerField(index=True)
    id_producto = IntegerField(index=True)
    stock_actual = IntegerField(default=0)
    stock_minimo = IntegerField(default=0)

    class Meta:
        table_name = 'ubicacion_almacenes'

    def consultar_capacidad_disponible(self):
        """Devuelve la capacidad disponible considerando el stock actual y mínimo."""
        return max(self.stock_actual - self.stock_minimo, 0)

from model import controlPlagas
from crud.crudProductosControl import create_producto, update_producto, delete_producto
from icrud import Icrud


class IcrudControlPlagas(Icrud):

	def create(self, **kwargs):
		return controlPlagas.ControlPlagas(kwargs['ica'], kwargs['nombre'], kwargs['frecuencia_aplicacion'], kwargs['valor'], kwargs['periodo_carencia'])
	

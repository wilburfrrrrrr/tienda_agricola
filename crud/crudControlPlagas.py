from model import controlPlagas
from crud.crudProductosControl import create_producto, update_producto, delete_producto
from icrud import Icrud


class IcrudControlPlagas(Icrud):
	lista_control_plagas = []

	def create(self, **kwargs):
		return controlPlagas.ControlPlagas(kwargs['ica'], kwargs['nombre'], kwargs['frecuencia_aplicacion'], kwargs['valor'], kwargs['periodo_carencia'])
	
	
# def read_control_plagas(ica):
# 	for control_plagas in lista_control_plagas:
# 		if control_plagas.ica == ica:
# 			return control_plagas
# 	raise Exception("No existe un control de plagas con el nombre indicado.")

	

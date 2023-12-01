from model import controlFertilizantes
from crud.crudProductosControl import create_producto, update_producto, delete_producto
from icrud import Icrud

class IcrudFertilizante(Icrud):
	lista_fertilizantes = []

	def create(self, **kwargs):
		return controlFertilizantes.ControlFertilizantes(kwargs['ica'], kwargs['nombre'], kwargs['frecuencia_aplicacion'], kwargs['valor'], kwargs['fecha_ultima_aplicacion'])
	
	# def read(self, **kwargs):

	



from model import controlFertilizantes
from icrud import Icrud

class IcrudFertilizante(Icrud):
	def create(self, **kwargs):
		return controlFertilizantes.ControlFertilizantes(kwargs['ica'], kwargs['nombre'], kwargs['frecuencia_aplicacion'], kwargs['valor'], kwargs['fecha_ultima_aplicacion'])
	
	



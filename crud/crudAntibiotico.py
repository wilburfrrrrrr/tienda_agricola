# import sys
# import os
# myDir = os.getcwd()
# sys.path.append(myDir)

from model.antibiotico import Antibiotico
from icrud import Icrud


class IcrudAntibiotico(Icrud):
	def create(self, **kwargs):
		return Antibiotico(kwargs['nombre'], kwargs['dosis'], kwargs['tipo_animal'], kwargs['valor'])



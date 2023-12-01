# import sys
# import os
# myDir = os.getcwd()
# sys.path.append(myDir)

from model.antibiotico import Antibiotico
from icrud import Icrud


class IcrudAntibiotico(Icrud):
	lista_antibioticos = []

	def create(self, **kwargs):
		return Antibiotico(kwargs['nombre'], kwargs['dosis'], kwargs['tipo_animal'], kwargs['valor'])


	# def verifica_antibiotico(nombre):
	# 	for antibiotico in lista_antibioticos:
	# 		if antibiotico.nombre == nombre:
	# 			raise Exception("Ya existe un antibiotico con el nombre indicado.")



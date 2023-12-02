from model.cliente import Cliente
from icrud import Icrud



class IcrudCliente(Icrud):
	def create(self, **kwargs):
		return Cliente(kwargs['nombre'], kwargs['cedula'])	
	

	def relation(self, **kwargs):
		Cliente.pedidos = kwargs['pedidos']
		return Cliente	


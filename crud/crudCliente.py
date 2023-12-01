from model.cliente import Cliente
from icrud import Icrud



class IcrudCliente(Icrud):
	lista_clientes = []
	def create(self, **kwargs):
		return Cliente(kwargs['nombre'], kwargs['cedula'])	
	
	# def read(self, **kwargs):
	# 	return read_cliente(kwargs['cedula'])

	def relation(self, **kwargs):
		Cliente.pedidos = kwargs['pedidos']
		return Cliente	

	def verifica_cliente(cedula):
		for cliente in lista_clientes:
			if cliente.cedula == cedula:
				raise Exception("Ya existe un cliente con la cedula indicada.")
			
	# def read_historial(cedula):
	# 	cliente = read_cliente(cedula)	
	# 	return cliente.historial_compras()

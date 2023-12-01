from crud import crudCliente
from crearClientes import ClienteController

class HistorialController():

	def buscar_cliente(cedula):
		for cliente in ClienteController.lista_clientes:
			if cliente.cedula == cedula:
				return cliente
		raise Exception("No se encontro un cliente con la cedula indicada.")
	
	def buscar_por_cedula(self, cedula):
		try:
			cliente = self.buscar_cliente(cedula)
			return cliente.pedidos
		except Exception as e:
			raise e

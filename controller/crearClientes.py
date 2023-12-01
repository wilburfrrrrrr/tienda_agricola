from crud import crudCliente

class ClienteController:

	lista_clientes = []

	def crearCliente(self, cedula, nombre):
		try:
			crudCliente.verifica_cliente(cedula)
			nuevo_cliente = crudCliente.crearCliente(cedula, nombre)
			self.lista_clientes.append(nuevo_cliente)
		except ValueError as e:
			raise e

	def buscar_cliente(self, cedula):
		for cliente in self.lista_clientes:
			if cliente.cedula == cedula:
				return cliente
		raise Exception("No existe un cliente con la cedula indicada.")
	
	def verificar_cedula(self, cedula):
		cliente = self.buscar_cliente(cedula)
		if cliente is None:
			return True
		else:
			raise Exception("Ya existe un cliente con la cedula indicada.")
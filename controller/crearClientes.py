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

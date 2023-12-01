from crud import crudPedidos, crudCliente
from comprarProductos import ProductoController

class PedidoController:
	def cargar_pedido(self, id_usuario, id_pedido, lista_productos):
		try:
			cliente = crudCliente.buscar_cliente(id_usuario)
			pedido = crudPedidos.crear_pedido(id_pedido, cliente, productos = ProductoController.lista_productos)
			crudCliente.IcrudCliente.relation(pedido = pedido)
			return pedido
		except Exception as e:
			raise e

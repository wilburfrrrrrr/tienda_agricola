from crud import crudPedidos, crudCliente
from comprarProductos import VentasController

class PedidoController:
	def cargar_pedido(self, id_usuario):
		try:
			cliente = crudCliente.buscar_cliente(id_usuario)
			pedido = crudPedidos.crear_pedido(cliente, productos = VentasController.lista_productos)
			crudCliente.IcrudCliente.relation(pedido = pedido)
			VentasController.vaciar_lista()
			return pedido
		except Exception as e:
			raise e

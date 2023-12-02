from model.pedido import Pedido
from icrud import Icrud


class IcrudPedido(Icrud):

	def create(self, **kwargs):
		return Pedido(kwargs['productos'])


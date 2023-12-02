from formularioBuscarHistorial import FormularioBuscarHistorial
from formularioComprarProductos import FormularioComprarProductos
from formularioCrearUsuario import FormularioCrearUsuario
from formularioCargarPedido import FormularioCargarPedido
from formularioMenuInicial import FormularioMenuInicial
from PyQt5.QtWidgets import QApplication, QStackedWidget
import sys

class FormularioPrincipal(QStackedWidget):
	def __init__(self):
		super().__init__()

		self.addWidget(FormularioMenuInicial())
		self.addWidget(FormularioCrearUsuario())
		self.addWidget(FormularioBuscarHistorial())
		self.addWidget(FormularioComprarProductos())
		self.addWidget(FormularioCargarPedido())	

		self.setCurrentIndex(0)

		FormularioMenuInicial.redirect_crear_usuario.connect(self.mostrar_formulario_crear_usuario)
		FormularioCrearUsuario.redirect_menu_inicial.connect(self.mostrar_formulario_menu_inicial)
		FormularioMenuInicial.redirect_buscar_historial.connect(self.mostrar_formulario_buscar_historial)
		FormularioBuscarHistorial.redirect_menu_inicial.connect(self.mostrar_formulario_menu_inicial)
		FormularioMenuInicial.redirect_comprar_productos.connect(self.mostrar_formulario_comprar_productos)
		FormularioComprarProductos.redirect_menu_inicial.connect(self.mostrar_formulario_menu_inicial)
		FormularioComprarProductos.redirect_cargar_pedido.connect(self.mostrar_formulario_cargar_pedido)
		FormularioCargarPedido.redirect_menu_inicial.connect(self.mostrar_formulario_menu_inicial)
		FormularioCargarPedido.redirect_comprar_productos.connect(self.mostrar_formulario_comprar_productos)

	def mostrar_formulario_menu_inicial(self):
		self.setCurrentIndex(0)

	def mostrar_formulario_crear_usuario(self):
		self.setCurrentIndex(1)

	def mostrar_formulario_buscar_historial(self):
		self.setCurrentIndex(2)

	def mostrar_formulario_comprar_productos(self):
		self.setCurrentIndex(3)

	def mostrar_formulario_cargar_pedido(self):
		self.setCurrentIndex(4)

if __name__ == '__main__':
	app = QApplication([])

	GUI = FormularioPrincipal()
	GUI.setWindowTitle('Administracion Vivero')
	GUI.show()
	sys.exit(app.exec_())
		

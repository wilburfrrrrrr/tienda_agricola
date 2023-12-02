import typing
from formularioBuscarHistorial import FormularioBuscarHistorial
from formularioComprarProductos import FormularioComprarProductos
from formularioCrearUsuario import FormularioCrearUsuario
from formularioCargarPedido import FormularioCargarPedido
from formularioMenuInicial import FormularioMenuInicial
from PyQt5.QtWidgets import QApplication, QStackedWidget, QWidget

class FormularioPrincipal(QStackedWidget):
	def __init__(self):
		super().__init__()

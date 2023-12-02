from forms import menu_inicial
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QVBoxLayout, QTextEdit, QPushButton, QLineEdit, QWidget, QStackedWidget
import sys
from formularioCrearUsuario import FormularioCrearUsuario
from formularioCargarPedido import FormularioCargarPedido
from formularioBuscarHistorial import FormularioBuscarHistorial
from formularioComprarProductos import FormularioComprarProductos

class FormularioMenuInicial(QMainWindow, menu_inicial.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.botonCrearUsuario.clicked.connect(self.crearUsuario)
		self.botonBuscarHistorial.clicked.connect(self.buscarHistorial)
		self.botonComprarProductos.clicked.connect(self.comprarProductos)
		
	def crearUsuario(self):
		from forms import formularioCrearUsuario
		self.formularioCrearUsuario = formularioCrearUsuario.FormularioCrearUsuario()
		self.formularioCrearUsuario.show()
	
	def cargarPedido(self):
		from forms import formularioCargarPedido
		self.formularioCargarPedido = formularioCargarPedido.FormularioCargarPedido()
		self.formularioCargarPedido.show()
	
	def buscarHistorial(self):
		from forms import formularioBuscarHistorial
		self.formularioBuscarHistorial = formularioBuscarHistorial.FormularioBuscarHistorial()
		self.formularioBuscarHistorial.show()
	
	def comprarProductos(self):
		from forms import formularioComprarProductos
		self.formularioComprarProductos = formularioComprarProductos.FormularioComprarProductos()
		self.formularioComprarProductos.show()
	
		
if __name__ == '__main__':
	app = QApplication(sys.argv)

	stacked_widget = QStackedWidget()
	stacked_widget.addWidget(FormularioMenuInicial())
	stacked_widget.addWidget(FormularioCrearUsuario())
	stacked_widget.addWidget(FormularioBuscarHistorial())
	stacked_widget.addWidget(FormularioComprarProductos())
	stacked_widget.addWidget(FormularioCargarPedido())	

	GUI = FormularioMenuInicial()
	GUI.setWindowTitle('Administracion Vivero')
	GUI.show()
	sys.exit(app.exec_())
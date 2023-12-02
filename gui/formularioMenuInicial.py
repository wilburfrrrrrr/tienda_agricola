from forms import menu_inicial
from PyQt5.QtWidgets import  QMainWindow
from PyQt5.QtCore import pyqtSignal


class FormularioMenuInicial(QMainWindow, menu_inicial.Ui_MainWindow):
	redirect_crear_usuario = pyqtSignal()
	redirect_comprar_productos = pyqtSignal()
	redirect_buscar_historial = pyqtSignal()
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.menu_inicial_pushButton_crear_cuenta.clicked.connect(self.crearUsuario)
		self.pushButton_historial.clicked.connect(self.buscarHistorial)
		self.menu_inicial_pushButton_compra.clicked.connect(self.comprarProductos)
		
	def crearUsuario(self):
		self.redirect_crear_usuario.emit()
	
	def buscarHistorial(self):
		self.redirect_buscar_historial.emit()
	
	def comprarProductos(self):
		self.redirect_comprar_productos.emit()
	

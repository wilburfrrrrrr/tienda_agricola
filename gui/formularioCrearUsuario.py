from forms import crear_usuario
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from controller.crearClientes import ClienteController
from PyQt5.QtCore import pyqtSignal

class FormularioCrearUsuario(QMainWindow, crear_usuario.Ui_MainWindow):
	redirect_menu_inicial = pyqtSignal()
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.registrar_crear.clicked.connect(self.crearUsuario)
		self.registrar_pushButton_volver.clicked.connect(self.volver)
		
	def crearUsuario(self):
		self.cedula = self.registrar_label_lineEdit_cedula.text()
		self.nombre = self.registrar_label_lineEdit_nombre.text()

		if self.cedula and self.nombre:
			ClienteController().crearCliente(self.cedula, self.nombre)
			emergente = QMessageBox()
			emergente.setIcon(QMessageBox.Information)
			emergente.setText("Cliente creado con exito")
			emergente.setWindowTitle("Informacion")
			emergente.exec_()
		else:
			emergente = QMessageBox()
			emergente.setIcon(QMessageBox.Warning)
			emergente.setText("Debe llenar todos los campos")
			emergente.setWindowTitle("Advertencia")
			emergente.exec_()
	
	def volver(self):
		self.registrar_label_lineEdit_nombre.clean()
		self.registrar_label_lineEdit_cedula.clean()
		self.redirect_menu_inicial.emit()
		
	

from forms import crear_usuario
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QVBoxLayout, QTextEdit, QPushButton, QLineEdit, QWidget, QStackedWidget
from controller.crearClientes import ClienteController
import sys

class FormularioCrearUsuario(QMainWindow, crear_usuario.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.registrar_crear	.clicked.connect(self.crearUsuario)
		self.registrar_pushButton_volver.clicked.connect(self.volver)
		
	def crearUsuario(self):
		self.cedula = self.cedula.text()
		self.nombre = self.nombre.text()

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
		self.cedula.setText("")
		self.nombre.setText("")
		self.apellido.setText("")
		self.textEdit.setText("")
		self.close()
	
if __name__ == '__main__':
	app = QApplication(sys.argv)
	GUI = FormularioCrearUsuario()
	GUI.setWindowTitle('Administracion Vivero')
	GUI.show()
	sys.exit(app.exec_())
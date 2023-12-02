from forms import cargar_productos
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QVBoxLayout, QTextEdit, QPushButton, QLineEdit, QWidget, QStackedWidget
from controller.cargarPedido import PedidoController
import sys

class FormularioCargarPedido(QMainWindow, cargar_productos.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.cargar_cuenta_pushButton_iniciar.clicked.connect(self.cargarPedido)
		self.cargar_cuenta_pushButton_volver.clicked.connect(self.volver)
		
	def cargarPedido(self):
		self.cedula = self.cargar_cuenta_lineEdit_cedula.text()
		if self.cedula:
			pedido = PedidoController().cargarPedido(self.cedula)
			if pedido != "":
				self.cargar_cuenta_lineEdit_cedula.clean()
				emergente = QMessageBox()
				emergente.setIcon(QMessageBox.Information)
				emergente.setText(pedido)
				emergente.exec_()
			else:
				emergente = QMessageBox()
				emergente.setIcon(QMessageBox.Warning)
				emergente.setText("El pedido no existe")
				emergente.setWindowTitle("Advertencia")
				emergente.exec_()
			self.ui.cargar_cuenta_lineEdit_cedula.clean
		else:
			emergente = QMessageBox()
			emergente.setIcon(QMessageBox.Warning)
			emergente.setText("Debe llenar todos los campos")
			emergente.setWindowTitle("Advertencia")
			emergente.exec_()
		
	
	def volver(self):
		self.cargar_cuenta_lineEdit_cedula.clean()
		self.cargar_cuenta_lineEdit_nombre.clean()
	
	

if __name__ == '__main__':
	app = QApplication(sys.argv)
	GUI = FormularioCargarPedido()
	GUI.setWindowTitle('Administracion Vivero')
	GUI.show()
	sys.exit(app.exec_())
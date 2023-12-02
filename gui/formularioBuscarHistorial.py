from forms import buscar_historial
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QVBoxLayout, QTextEdit, QPushButton, QLineEdit, QWidget, QStackedWidget
from controller.buscarCedula import HistorialController
import sys

class FormularioBuscarHistorial(QMainWindow, buscar_historial.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.botonBuscar.clicked.connect(self.buscarCedula)
		self.botonVolver.clicked.connect(self.volver)
		self.botonSalir.clicked.connect(self.salir)
		
	def buscarCedula(self):
		self.cedula = self.buscar_historial_lineEdit_cedula.text()
		if self.cedula:
			historial = HistorialController.buscar_por_cedula(self.cedula)
			if historial != "":
				self.buscar_historial_lineEdit_cedula.clean()
				emergente = QMessageBox()
				emergente.setIcon(QMessageBox.Information)
				emergente.setText(historial)
				emergente.exec_()
			else:
				emergente = QMessageBox()
				emergente.setIcon(QMessageBox.Warning)
				emergente.setText("El historial no existe")
				emergente.setWindowTitle("Advertencia")
				emergente.exec_()	
		else:
			emergente = QMessageBox()
			emergente.setIcon(QMessageBox.Warning)
			emergente.setText("Debe llenar todos los campos")
			emergente.setWindowTitle("Advertencia")
			emergente.exec_()	

	def volver(self):
		self.ui.cedula.setText("")
		self.ui.textEdit.setText("")
		self.close()
	
	

if __name__ == '__main__':
	app = QApplication(sys.argv)
	GUI = FormularioBuscarHistorial()
	GUI.setWindowTitle('Administracion Vivero')
	GUI.show()
	sys.exit(app.exec_())
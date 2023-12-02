from forms import buscar_historial
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal
from controller.buscarCedula import HistorialController

class FormularioBuscarHistorial(QMainWindow, buscar_historial.Ui_MainWindow):
	redirect_menu_inicial = pyqtSignal()
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.buscarCedula)
		self.buscar_historial_pushButton_volver.clicked.connect(self.volver)
		
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
		self.buscar_historial_lineEdit_cedula.clean()
		self.redirect_menu_inicial.emit()
	

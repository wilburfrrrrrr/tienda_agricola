from forms import menu_compras_usuario
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QVBoxLayout, QTextEdit, QPushButton, QLineEdit, QWidget, QStackedWidget
from controller.comprarProductos import ventasController
import sys
from formularioMenuInicial import FormularioMenuInicial

class FormularioComprarProductos(QMainWindow, menu_compras_usuario.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.control_plaga_pushButtom_comprar.clicked.connect(self.comprarProductos)
		self.antibiotico_pushButton.clicked.connect(self.comprarProductos)
		self.fertilizantes_pushButton_comprar.clicked.connect(self.comprarProductos)
		self.cargar_pedido.clicked.connect(self.comprarProductos)
		self.principal_pushButton_volver.clicked.connect(self.volver)
		
	def comprarAntibiotico(self):
		self.nombre = self.antibiotico_lineEdit_nombre.text()
		self.dosis = self.antibiotico_lineEdit_dosis.text()
		self.tipo_animal = self.antibiotico_lineEdit_tipo_animal.text()
		self.valor = self.antibiotico_comboBox_valor.text()

		if self.nombre and self.dosis and self.tipo_animal and self.valor:
			ventasController().comprarAntibiotico( self.nombre, self.dosis, self.tipo_animal, self.valor)

			
			self.antibiotico_lineEdit_nombre.clear()
			self.antibiotico_lineEdit_dosis.clear()
			self.antibiotico_lineEdit_tipo_animal.clear()
			self.antibiotico_comboBox_valor.clear()


			emergente = QMessageBox()
			emergente.setIcon(QMessageBox.Information)
			emergente.setText("Finca agregada con exito")
			emergente.setWindowTitle("Informacion")
			emergente.exec_()
		else:
			emergente = QMessageBox()
			emergente.setIcon(QMessageBox.Warning)
			emergente.setText("Debe llenar todos los campos")
			emergente.setWindowTitle("Advertencia")
			emergente.exec_()

	def comprarControlPlaga(self):
		self.nombre = self.control_plaga_lineEdit_nombre.text()
		self.ica = self.control_plaga_lineEdit_ica.text()
		self.frecuencia = self.control_plaga_lineEdit_frecuecia_2.text()
		self.valor = self.control_plaga_lineEdit_valor.text()
		self.periodo_carencia = self.control_plaga_lineEdit_periodo_carencia.text

		if self.nombre and self.ica and self.frecuencia and self.valor and self.periodo_carencia:
			ventasController().comprarControlPlaga( self.nombre, self.ica, self.frecuencia, self.valor, self.periodo_carencia)

			self.control_plaga_lineEdit_nombre.clear()
			self.control_plaga_lineEdit_dosis.clear()
			self.control_plaga_lineEdit_tipo_animal.clear()
			self.control_plaga_comboBox_valor.clear()

			emergente = QMessageBox()
			emergente.setIcon(QMessageBox.Information)
			emergente.setText("Finca agregada con exito")
			emergente.setWindowTitle("Informacion")
			emergente.exec_()
		else:
			emergente = QMessageBox()
			emergente.setIcon(QMessageBox.Warning)
			emergente.setText("Debe llenar todos los campos")
			emergente.setWindowTitle("Advertencia")
			emergente.exec_()

	def comprarFertilizante(self):
		self.nombre = self.fertilizante_lineEdit_nombre.text()
		self.ica = self.fertilizante_lineEdit_ica.text()
		self.frecuencia = self.fertilizante_lineEdit_frecuencia.text()
		self.valor = self.fertilizante_lineEdit_valor.text()
		self.fecha = self.fertilizante_lineEdit_fecha.text()

		if self.nombre and self.ica and self.frecuencia and self.valor and self.fecha:
			ventasController().comprarFertilizante( self.nombre, self.ica, self.frecuencia, self.valor, self.fecha)

			self.fertilizante_lineEdit_nombre.clear()
			self.fertilizante_lineEdit_dosis.clear()
			self.fertilizante_lineEdit_tipo_animal.clear()
			self.fertilizante_comboBox_valor.clear()

			emergente = QMessageBox()
			emergente.setIcon(QMessageBox.Information)
			emergente.setText("Finca agregada con exito")
			emergente.setWindowTitle("Informacion")
			emergente.exec_()
		else:
			emergente = QMessageBox()
			emergente.setIcon(QMessageBox.Warning)
			emergente.setText("Debe llenar todos los campos")
			emergente.setWindowTitle("Advertencia")
			emergente.exec_()

	def volver(self):
		self.fertilizante_lineEdit_nombre.clear()
		self.fertilizante_lineEdit_dosis.clear()
		self.fertilizante_lineEdit_tipo_animal.clear()
		self.fertilizante_comboBox_valor.clear()
		self.close()

	def cargarPedido(self):
		#redirect to the form to load a pedido
		pass

if __name__ == '__main__':
	app = QApplication(sys.argv)
	

	GUI = FormularioComprarProductos()
	GUI.setWindowTitle('Administracion Vivero')
	GUI.show()
	sys.exit(app.exec_())
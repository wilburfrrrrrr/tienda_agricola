from forms import menu_compras_usuario
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal
from controller.comprarProductos import VentasController


class FormularioComprarProductos(QMainWindow, menu_compras_usuario.Ui_MainWindow):
	redirect_menu_inicial = pyqtSignal()
	redirect_cargar_pedido = pyqtSignal()
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.control_plaga_pushButtom_comprar.clicked.connect(self.comprarControlPlaga)
		self.antibiotico_pushButton.clicked.connect(self.comprarAntibiotico)
		self.fertilizantes_pushButton_comprar.clicked.connect(self.comprarFertilizante)
		self.cargar_pedido.clicked.connect(self.cargarPedido)
		self.principal_pushButton_volver.clicked.connect(self.volver)
		
	def comprarAntibiotico(self):
		self.nombre = self.antibiotico_lineEdit_nombre.text()
		self.dosis = self.antibiotico_lineEdit_dosis.text()
		self.tipo_animal = self.antibiotico_lineEdit_tipo_animal.text()
		self.valor = self.antibiotico_comboBox_valor.text()

		if self.nombre and self.dosis and self.tipo_animal and self.valor:
			VentasController().comprarAntibiotico( self.nombre, self.dosis, self.tipo_animal, self.valor)

			self.antibiotico_lineEdit_nombre.clear()
			self.antibiotico_lineEdit_dosis.clear()
			self.antibiotico_lineEdit_tipo_animal.clear()
			self.antibiotico_comboBox_valor.clear()

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
		self.periodo_carencia = self.control_plaga_lineEdit_periodo_carencia.text()

		if self.nombre and self.ica and self.frecuencia and self.valor and self.periodo_carencia:
			VentasController().comprarControlPlaga( self.nombre, self.ica, self.frecuencia, self.valor, self.periodo_carencia)

			self.control_plaga_lineEdit_nombre.clean()
			self.control_plaga_lineEdit_ica.clean()
			self.control_plaga_lineEdit_frecuecia_2.clean()
			self.control_plaga_lineEdit_valor.clean()
			self.control_plaga_lineEdit_periodo_carencia.clean()

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
			VentasController().comprarFertilizante( self.nombre, self.ica, self.frecuencia, self.valor, self.fecha)

			self.fertilizante_lineEdit_nombre.clean()
			self.fertilizante_lineEdit_ica.clean()
			self.fertilizante_lineEdit_frecuencia.clean()
			self.fertilizante_lineEdit_valor.clean()
			self.fertilizante_lineEdit_fecha.clean()

		else:
			emergente = QMessageBox()
			emergente.setIcon(QMessageBox.Warning)
			emergente.setText("Debe llenar todos los campos")
			emergente.setWindowTitle("Advertencia")
			emergente.exec_()


	def cargarPedido(self):
		self.fertilizante_lineEdit_nombre.clean()
		self.fertilizante_lineEdit_ica.clean()
		self.fertilizante_lineEdit_frecuencia.clean()
		self.fertilizante_lineEdit_valor.clean()
		self.fertilizante_lineEdit_fecha.clean()
		self.control_plaga_lineEdit_nombre.clean()
		self.control_plaga_lineEdit_ica.clean()
		self.control_plaga_lineEdit_frecuecia_2.clean()
		self.control_plaga_lineEdit_valor.clean()
		self.control_plaga_lineEdit_periodo_carencia.clean()		
		self.antibiotico_lineEdit_nombre.clear()
		self.antibiotico_lineEdit_dosis.clear()
		self.antibiotico_lineEdit_tipo_animal.clear()
		self.antibiotico_comboBox_valor.clear()
		self.redirect_cargar_pedido.emit()

	def volver(self):
		self.fertilizante_lineEdit_nombre.clean()
		self.fertilizante_lineEdit_ica.clean()
		self.fertilizante_lineEdit_frecuencia.clean()
		self.fertilizante_lineEdit_valor.clean()
		self.fertilizante_lineEdit_fecha.clean()
		self.control_plaga_lineEdit_nombre.clean()
		self.control_plaga_lineEdit_ica.clean()
		self.control_plaga_lineEdit_frecuecia_2.clean()
		self.control_plaga_lineEdit_valor.clean()
		self.control_plaga_lineEdit_periodo_carencia.clean()		
		self.antibiotico_lineEdit_nombre.clear()
		self.antibiotico_lineEdit_dosis.clear()
		self.antibiotico_lineEdit_tipo_animal.clear()
		self.antibiotico_comboBox_valor.clear()
		self.redirect_menu_inicial.emit()



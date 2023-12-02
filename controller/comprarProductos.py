from crud import crudControlFertilizantes, crudControlPlagas, crudAntibiotico

class ventasController:
	lista_productos = []
	def crearFertilizante(self, ica, nombre, frecuencia, valor, fecha):
		try:
			# crudControlFertilizantes.verifica_producto(ica)
			nuevo_producto = crudControlFertilizantes.crearProducto(ica = ica, nombre = nombre, frecuencia_aplicacion = frecuencia, valor = valor, fecha_ultima_aplicacion = fecha)
			# self.lista_productos.append(nuevo_producto)
		except ValueError as e:
			raise e
		
	def crearPlaga(self, ica, nombre, frecuencia, valor, periodo):
		try:
			# crudControlPlagas.verifica_producto(ica)
			nuevo_producto = crudControlPlagas.crearProducto(ica = ica, nombre = nombre, frecuencia_aplicacion = frecuencia, valor = valor, periodo_carencia = periodo)
			# self.lista_productos.append(nuevo_producto)
		except ValueError as e:
			raise e
		
	def crearAntibiotico(self, nombre, dosis, tipo_animal, valor):
		try:
			# crudAntibiotico.verifica_producto(nombre)
			nuevo_producto = crudAntibiotico.crearProducto(nombre = nombre, dosis = dosis, tipo_animal = tipo_animal, valor = valor)
			# self.lista_productos.append(nuevo_producto)
		except ValueError as e:
			raise e
		
	def vaciar_lista(self):
		self.lista_productos = []
	
class Cliente:
    def __init__(self, nombre, cedula):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__pedidos = []

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if not nombre.isalpha():
            raise ValueError("El nombre debe contener solo letras.")
        self.__nombre = nombre
        
    @property
    def cedula(self):
        return self.__cedula
    
    @cedula.setter
    def cedula(self, cedula):
        if not cedula.isdigit():
            raise ValueError("La cédula debe contener solo números.")
        self.__cedula = cedula
        
    @property
    def pedidos(self):
        return self.__pedidos
    
    @pedidos.setter
    def pedidos(self, pedidos):
        self.__pedidos.append(pedidos)

    def historial_compras(self):
        return self.pedidos
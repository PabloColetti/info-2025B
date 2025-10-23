class Vehiculo:
    contador_vehiculo = 0

    # CONSTRUCTOR
    def __init__(self, param_marca, param_modelo, param_estado):  # this
        # PUBLICO
        self.marca = param_marca
        # PUBLICO
        self.modelo = param_modelo
        # PROTEGIDO acceder/modificar en la propia clase o en una clase hija
        self._estado = param_estado
        # PRIVADO acceder/modificar en la propia clase
        self.__id_vehiculo = Vehiculo.contador_vehiculo + 1

        Vehiculo.contador_vehiculo += 1

    def __str__(self):
        return f"Soy un vehiculo marca: {self.marca}, modelo: {self.modelo} en estado: {self._estado}, con id: {self.__id_vehiculo}"

    # @property
    def get_estado(self):
        return self._estado

    def set_estado(self, param_nuevo_estado):
        self._estado = param_nuevo_estado

    def get_id_vehiculo(self):
        return self.__id_vehiculo
    
    @classmethod
    def get_contador_vehiculo(cls):
        return cls.contador_vehiculo
    
    @staticmethod
    def calcular_costo_reparacion(hs_trabajo, hs_por_hora):
        return hs_trabajo * hs_por_hora
    


#### PUBLICO ####

camion = Vehiculo("Mercedez", "1114", "Bueno")
cuatri = Vehiculo("Honda", "x", "Impecable")
auto = Vehiculo("Toyota", "Corolla", "Impecable")

# print(camion.marca)
# print(camion.modelo)

# print(camion._estado)                 # NO ES CORRECTO
print(camion.get_estado())            # ES CORRECTO

# camion._estado = "Impecable"          # NO ES CORRECTO
# camion.set_estado("Impecable")        # ES CORRECTO

# print(camion.get_estado())            # ES CORRECTO

# print(camion._Vehiculo__id_vehiculo)  # NO ES CORRECTO
# print(camion.get_id_vehiculo())       # ES CORRECTO
# print(camion.get_contador_vehiculo()) # ES CORRECTO

# print(cuatri.get_id_vehiculo())       # ES CORRECTO
# print(cuatri.get_contador_vehiculo())

# print(auto.get_contador_vehiculo())

# print(auto.calcular_costo_reparacion(4, 15000))
# print(camion.calcular_costo_reparacion(8, 20000))

print(camion)
print(cuatri)
print(auto)
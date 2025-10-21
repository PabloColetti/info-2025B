class Vehiculo:
    # CONSTRUCTOR
    def __init__(self, param_marca, param_modelo, param_color):
        self.marca = param_marca
        self.modelo = param_modelo
        self.color = param_color

    # METODOS
    def mostrar_info(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}"


class Auto(Vehiculo):
    def __init__(self, param_marca, param_modelo, param_color, param_num_puertas):
        super().__init__(param_marca, param_modelo, param_color)
        self.num_puertas = param_num_puertas

    def mostrar_info(self):
        return f"Tengo un {self.marca} {self.modelo} {self.color} de {self.num_puertas} puertas"


class Moto(Vehiculo):
    def __init__(self, param_marca, param_modelo, param_color, param_cilindrada):
        super().__init__(param_marca, param_modelo, param_color)
        self.cilindrada = param_cilindrada

    def mostrar_info(self):
        return f"Tengo una {self.marca} {self.modelo} {self.cilindrada} {self.color}"


# auto = Vehiculo("Jeep", "Compass", "Blanco")
auto = Auto("Jeep", "Compass", "Blanco", 5)
moto = Moto("Kawasaki", "Ninja", "Verde", "1000cc")
camion = Vehiculo("Mercedez", "1114", "Azul")

# print(auto)
print(auto.mostrar_info())
print(moto.mostrar_info())
print(camion.mostrar_info())

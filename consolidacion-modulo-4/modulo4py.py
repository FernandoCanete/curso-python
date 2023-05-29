class Vehiculo:
    def __init__(self, marca, modelo, num_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, num_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

class Particular(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, num_puestos):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.num_puestos = num_puestos

class Carga(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, tipo):
        super().__init__(marca, modelo, num_ruedas)
        self.tipo = tipo

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, num_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, num_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

# se crean instancias
particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

# se imprime la informacion de las instancias
print(f"Marca {particular.marca}, Modelo {particular.modelo}, {particular.num_ruedas} ruedas {particular.velocidad} Km/h, {particular.cilindrada} cc Puestos: {particular.num_puestos}")
print(f"Marca {carga.marca}, Modelo {carga.modelo}, {carga.num_ruedas} ruedas {carga.velocidad} Km/h, {carga.cilindrada} cc Carga: {carga.peso_carga} Kg")
print(f"Marca {bicicleta.marca}, Modelo {bicicleta.modelo}, {bicicleta.num_ruedas} ruedas Tipo: {bicicleta.tipo}")
print(f"Marca {motocicleta.marca}, Modelo {motocicleta.modelo}, {motocicleta.num_ruedas} ruedas Tipo: {motocicleta.tipo} Motor: {motocicleta.motor}, Cuadro: {motocicleta.cuadro}, Nro Radios: {motocicleta.nro_radios}")




class Cine:
    def __init__(self, nombre, rut, direccion):
        self.nombre = nombre
        self.rut = rut
        self.direccion = direccion

class Sala:
    def __init__(self, numero, asientos, horarios):
        self.numero = numero
        self.asientos = asientos
        self.horarios = horarios

class Pelicula:
    def __init__(self, nombre, salas, horarios):
        self.nombre = nombre
        self.salas = salas
        self.horarios = horarios

class Boletos:
    def __init__(self, tipo, asientos_vendidos):
        self.tipo = tipo
        self.asientos_vendidos = asientos_vendidos

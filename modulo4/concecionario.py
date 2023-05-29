#autos y motos, bicicletas
#autos [color, tipo_motor, ruedas, cantidad_puertas, tipo_freno, tipo_encendido]
#motos[color, tipo_motor, ruedas, tipo_freno, tipo_encendido, tipo_cadena]
#bicicletas[color, marca, modelo, ruedas, tipo_freno, tipo_manubrio]




class Vehiculo:
    def __init__(self, _color, _ruedas, _tipo_freno):
        self.color = _color
        self.ruedas = _ruedas
        self.tipo_freno = _tipo_freno

class Auto(Vehiculo):
    def __init__(self, _color, _ruedas, _tipo_freno, _tipo_motor, _tipo_encendido):
        super(). __init__(self, _color, _ruedas, _tipo_freno)
        self.tipo_motor = _tipo_motor
        self.tipo_encendido = _tipo_encendido
    
class Moto(Vehiculo):
    def __init__(self, _color, _ruedas, _tipo_freno, _tipo_motor, _tipo_encendido, _tipo_cadena):
        super(). __init__(self, _color, _ruedas, _tipo_freno)
        self.tipo_motor = _tipo_motor
        self.tipo_encendido = _tipo_encendido
        self.tipo_cadena = _tipo_cadena

class Bicicleta(Vehiculo):
    def __init__(self, _color, _ruedas, _tipo_freno, _tipo_manubrio):
        super(). __init__(self, _color, _ruedas, _tipo_freno)
        self.tipo_mmanubrio = _tipo_manubrio
             
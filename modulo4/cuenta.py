class Cuenta:
    def __init__(self, _titular, _cuenta_numero, _saldo):
        self.titular = _titular
        self.cuenta_numero =_cuenta_numero
        self.saldo = _saldo
        

class PlazoFijo(Cuenta):
    def __init__(self, _titular, _cuenta_numero, _saldo, _plazo, _interes):
        super().__init__(self, _titular, _cuenta_numero, _saldo)
        self.plazo = _plazo
        self.interes = _interes

class CajaAhorro(Cuenta):
    def __init__(self):
        super().__init__()
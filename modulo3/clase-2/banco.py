class Banco:
    cuentas = [] #guardar las cuentas y correlativos
    movimientos = [] #guardar los movimientos

    def __init__(self):
        pass

    def agregar_cuenta(self, _cuenta, _rut):
        self.cuentas.append({
            "cuenta" : _cuenta,
            "rut" : _rut,
            "correlativo_movimiento" : 1,
            "saldo" : 0
        })

        def agregar_movimiento(self, _cuenta, _fecha, _tipo, _monto):
            for elemento in self.cuentas:
                if elemento["numero_cuenta"] == _cuenta:
                    if _tipo == "retiro":
                        if elemento["saldo"] - _monto < 0:
                            print("saldo insuficiente")
                        else:
                            self.movimientos.append({
                                "cuenta": _cuenta,
                                "fecha" : _fecha,
                                "tipo" : _tipo,
                                "monto" : _monto,
                                "saldo" : elemento["saldo"] - _monto

                            } )    

                break



banco_bci = Banco()

banco_bci.agregar_cuenta("7360001", "14.999.000-1")
banco_bci.agregar_cuenta("7360002", "14.999.000-2")
banco_bci.agregar_cuenta("7360003", "14.999.000-3")
banco_bci.agregar_cuenta("7360004", "14.999.000-4")

print(Banco.cuentas)


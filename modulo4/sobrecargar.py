class Persona:
    message_base = "te estoy llamando"
    def __init__(self,_name):
        self.name = _name

    def llamar(self):
        print("te estoy llamando")

    def llamar(self, _medio=''):
        message = "te estoy llamando"
        if (_medio != ''):
            message = f"te estoy llamando con {_medio}"
        print(message)

    def llamar(self. _medio='', _time= ''):
        message = self.message_base
        if (_medio != '' and _time == ''):
            message = f"{self.message_base} con {_medio}"
        if (_medio != '' and _time != ''):
            message = f"{self.message_base} con {_medio} a las {_time}" 
        print(message)  


juan = Persona("Juan")

juan.llamar("telefonp")


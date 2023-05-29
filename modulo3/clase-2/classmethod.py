class Empleado:
    sueldo_base = 100.000
    
    def __init__(self, _name):
        self.__name =_name
        
        @property 
        def name(self):
            return self._name
        
        name.setter
        def name(self._name):
            self._name = _name

        @classmethod
        def get_sueldo_base(cls, _sueldo):
            cls.sueldo_base = _sueldo


    
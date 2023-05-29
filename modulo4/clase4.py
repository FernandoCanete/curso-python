class Padre:
    def __init__(self, _name_padre, _rut_padre):
        self.name = _name_padre
        self.rut = _rut_padre
        self.sueldo = 0

    def pintar(self):
        print("estoy pintando")

class Hijo(Padre):
    def __init__(self, _name_hijo, _color_ojos):
       Padre.__init__(self, _name_hijo)
       self.color_ojos = _color_ojos

    def lijar(self):
        print(f"{self.name} esta lijando")
        
richar = Padre("Richar Lujano", "1")

richard = Hijo("Richard Lujano", "2", "Marron")


print(richar.name, richar.sueldo)
print(richard.name, richard.sueldo)

richard.pintar()
richard.pintar()
richard.lijar()
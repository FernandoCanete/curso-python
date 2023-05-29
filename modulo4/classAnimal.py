class Animal():
    def __init__(self, _nombre, _raza, _edad, _peso):
        self.nombre = _nombre
        self.raza = _raza
        self.edad = _edad
        self.peso = _peso

    def comer(self):
        print(f"{self.nombre} esta comiendo")

    def caminar(self):
        print(f"{self.nombre} esta caminando")

    def dormir(self):
        print(f"{self.nombre} esta durmiendo")

class Perro(Animal):
    def __init__(self, _nombre, _raza, _edad, _peso):
        super().__init__(_nombre, _raza, _edad, _peso)

    def ladrar(self):
        print(f"{self.nombre} está ladrando")

class Gato(Animal):
    def __init__(self, _nombre, _raza, _edad, _peso):
        super().__init__(_nombre, _raza, _edad, _peso)

    def maullar(self):
        print(f"{self.nombre} está maullando")

perro = Perro("Nasus", "San Bernardo", 3, 30)
gato = Gato("Rengar", "Persa", 4, 3)


print(f"Nombre del perro: {perro.nombre}")
print(f"Raza del perro: {perro.raza}")
print(f"Edad del perro: {perro.edad}")
print(f"Peso del perro: {perro.peso}")

print(f"Nombre del gato: {gato.nombre}")
print(f"Raza del gato: {gato.raza}")
print(f"Edad del gato: {gato.edad}")
print(f"Peso del gato: {gato.peso}")

        
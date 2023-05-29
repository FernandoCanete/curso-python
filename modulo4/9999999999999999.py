class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

    def hacer_sonido(self):
        raise TypeError("¡Error de tipo! No se puede llamar al método 'hacer_sonido' en la clase base 'Animal'.")

# Crear una instancia de la clase Animal
mi_animal = Animal("Fido", 3)

# Llamar al método hacer_sonido generará un error TypeError
mi_animal.hacer_sonido()
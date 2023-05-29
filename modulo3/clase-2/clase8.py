class animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type


gato = animal("Angora", "Persa")
print(gato.type)
gato.type = "Grandanes"
print(gato.type)


class Droid:
    def __init__(self, name):
        self.hidden_name = name

        @property 
        def name(self) -> str:
            return self.hidden_name
        
        @name.setter
        def name(self, name:str) ->None:
            self.hidden_name = name


android = Droid("arthur")

print(android)
android.name = "Citripio"
print(android.name)

#android.hidden.name = "rojo"
#print(android.hidden_name)
print(android.name)

print("/n**********************/n")
class CalculatedValue:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    @property
    def get_calculated_value(self) -> float:
        return 0.35 * self.height
    
valuex = CalculatedValue("ratio", 10)

print(f"El {valuex.name} es: {valuex.get_calculate_value}")

    
        


#creando una clase
class Transporte:
    pass

#instancias la clases y crear un objeto
transporte1 = Transporte()
transporte2 = Transporte()

class BuzzeLightYear:
    pass

bozz1 = BuzzeLightYear()
bozz2 = BuzzeLightYear()

print(type(transporte1))
print(type(bozz1))

class Droid:
    def switch_on(self):
        print("hola soy un droid, y estoy a tu orden")
        self.power_on = True

    def switch_off(self):
        print("Adios, enciendeme, cuando me necesites")
        self.power_on = False

k8_arthur = Droid() 
k8_citripio = Droid()

k8_arthur.switch_on()
print("power on Arthur:", k8_arthur.power_on)
k8_arthur.switch_off()
print("power on citripio:", k8_arthur.power_on)
k8_arthur.switch_off()
print(k8_arthur.power_on)

class Vehicle:
    def __init__(self, type, model):
        self.type_vehicle = type
        self.model_vehicle = model

sedan = Vehicle("sedan", "aveo")
print(sedan.type_vehicle, sedan.model_vehicle)
pickup =Vehicle("pickup","ranger")
print(pickup.type_vehicle, pickup.model_vehicle)

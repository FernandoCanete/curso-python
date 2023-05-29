class Vehiculo():
    #atributos
    modelo = ""
    marca = ""
    color = ""
    velocidad = ""
    nro_puertas = 0
    kilometraje = 0
    arrancando = False
    
    #metodos

    def encender(self):
        pass
        

    def apagar(self):
        pass

    def acelerar(self):
        pass

    def frenar(self):
        pass

objeto_carro1 = Vehiculo()    
print(objeto_carro1.color)
objeto_carro1.encender()
objeto_carro1.color = "Gris"
print(objeto_carro1.color)
   


class Motocicleta:
    is_new = True

    def __init__(self,_color,_matricula,_combustible_litros,_numero_ruedas, 
                 _marca,_modelo ,_fecha_fabricacion,_velocidad,_velocidad_punta,_peso):

        self.color = _color
        self.matricula = _matricula
        self.combustible_litros = _combustible_litros
        self.numero_ruedas = _numero_ruedas
        self.marca = _marca
        self.modelo = _modelo
        self.fecha_fabricacion = _fecha_fabricacion
        self.velocidad_punta = _velocidad_punta
        self.peso = _peso

#if self.variable == False: === if not self.variable:
#if self.variable == True: === if self.variable

    def arrancar(self):
        if not self.motor:
            print("El motor ya estabaen marcha")
        else:
            print("El motor ya ha arrancado")

def detener(self):
    if not self.motor:
        print("El motor ya estaba detenido")
    else:
        print("El motor se ha apagado")
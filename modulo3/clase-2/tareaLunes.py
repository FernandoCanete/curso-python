class Torniquete():
    # ATRIBUTOS  DE LOS OBJETOS DE LA CLASE TORNIQUETE
    def __init__(self, patente):   
        self.patente = patente
        self.adultos_pagados = 0
        self.niños_pagados = 0
        self.adultos_mayores_pagados = 0
        self.recaudado = 0
    
    # ESTOS 3 METODOS AUMENTAN CONTADORES EN 1 Y SE AUMENTA EL MONTO EN ADULTO EN 730, NIÑO EN 0 Y ADULTO MAYOR 365
    def agregar_adulto(self):
        self.adultos_pagados += 1
        self.recaudado += 730
        
    def agregar_niño(self):
        self.niños_pagados += 1 
    
    def agregar_adulto_mayor(self):
        self.adultos_mayores_pagados += 1
        self.recaudado += 365
    
    # ESTE METODO IMPRIME UN REPORTE DE LA CANTIDAD DE CONTADORES Y EL MONTO RECAUDADO.

    def reporte_diario(self):
        print("Reporte diario de la micro", self.patente)
        print("Adultos pagados:", self.adultos_pagados)
        print("Niños pagados:", self.niños_pagados)
        print("Adultos mayores pagados:", self.adultos_mayores_pagados)
        print("Total recaudado:", self.recaudado)

# CREACION DE 2 OBJETOS, EN ESTE CASO MICROS CON DISTINTAS PATENTES
microbus1 = Torniquete("AABB-22")
microbus1.agregar_adulto()
microbus1.agregar_adulto()
microbus1.agregar_niño()
microbus1.agregar_adulto_mayor()
microbus1.reporte_diario()

microbus2 = Torniquete("CCDD-33")
microbus2.agregar_adulto()
microbus2.agregar_adulto()
microbus2.agregar_adulto()
microbus2.agregar_adulto()
microbus2.agregar_adulto()
microbus2.agregar_adulto()
microbus2.agregar_adulto()
microbus2.agregar_adulto()
microbus2.agregar_adulto()
microbus2.agregar_adulto_mayor()
microbus2.agregar_adulto_mayor()
microbus2.agregar_adulto_mayor()
microbus2.agregar_adulto_mayor()
microbus2.reporte_diario()


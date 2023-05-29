
class Cine:
    def __init__(self, nombre, rut, direccion):
        self.nombre = nombre
        self.rut = rut
        self.direccion = direccion

class Sala:
    def __init__(self, numero, asientos, horarios):
        self.numero = numero
        self.asientos = asientos
        self.horarios = horarios

class Pelicula:
    def __init__(self, nombre, salas, horarios):
        self.nombre = nombre
        self.salas = salas
        self.horarios = horarios

class Boletos:
    def __init__(self, tipo, asientos_vendidos):
        self.tipo = tipo
        self.asientos_vendidos = asientos_vendidos

def vender_boletos(pelicula, sala, horario, tipo_boleto, asiento):
    # Verificar que el asiento no esté vendido
    if asiento in boletos.asientos_vendidos:
        print("Lo sentimos, ese asiento ya fue vendido.")
    else:
        # Asignar el asiento
        boletos.asientos_vendidos.append(asiento)

        # Registar la venta de boletos
        if tipo_boleto == "normal":
            venta_normal = venta_normal + 1
        else:
            venta_vip = venta_vip + 1

def reporte_diario():
    # Obtener la cantidad de boletos vendidos por día
    for dia in range(1, 31): # Suponiendo que el cine está abierto los 30 días del mes
        boletos_vendidos = 0
        for pelicula in cartelera[dia]:
            for sala in pelicula.salas:
                for horario in sala.horarios:
                    for boleto in horario.boletos:
                        boletos_vendidos = boletos_vendidos + len(boleto.asientos_vendidos)
            print("El día", dia, "se vendieron", boletos_vendidos, "entradas")

def reporte_entradas_funcion(pelicula, sala, horario):
    # Obtener la cantidad de boletos vendidos para una función específica
    boletos_vendidos = 0
    for boleto in horario.boletos:
        boletos_vendidos = boletos_vendidos + len(boleto.asientos_vendidos)
    print("Para la función de la película", pelicula, "en la sala", sala, "a las", horario, "se vendieron", boletos_vendidos, "entradas")

def reporte_entradas_pelicula(pelicula):
    # Obtener la cantidad de boletos vendidos para una película específica
    boletos_vendidos = 0
    for dia in range(1, 31):
        for horario in pelicula.horarios:
            for sala in pelicula.salas:
                for boleto in horario.boletos:
                    boletos_vendidos = boletos_vendidos + len(boleto.asientos_vendidos)
    print("Para la película", pelicula, "se vendieron", boletos_vendidos, "boletos en total")

def reporte_entradas_dia(dia):
    # Obtener la cantidad de boletos vendidos para todas las películas en un día específico
    boletos_vendidos = 0
    for pelicula in cartelera[dia]:
        for horario in pelicula.horarios:
            for sala in pelicula.salas:
                for boleto in horario.boletos:
                    boletos_vendidos = boletos_vendidos + len(boleto.asientos_vendidos)
        print("Para el día", dia, "la película", pelicula.nombre, "se vendieron", boletos_vendidos, "boletos")


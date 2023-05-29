class CustomErrorException(Exception): 
    def __init__(self, numero): 
        mensaje = f"Error: {numero} no es un número válido. Solo se permiten los números 4, 5 y 6."
        super().__init__(mensaje)


def verificar_numero():
    numero = int(input("ingrese un numero:"))
    if numero not in [4, 5, 6]:
        raise CustomErrorException(numero) 
    else:
        print(" Si pertenece a uno de los siguientes Subconjuntos: [], [4], [5], [6] , [4, 5], [4, 6] ,[5, 6], [4, 5, 6]")
try:
    verificar_numero()
except CustomErrorException as error:
    print(error)


 
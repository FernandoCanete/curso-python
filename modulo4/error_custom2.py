class NoPuedeEscribirDosException(Exception):
    def __init__(self, _message):
        self.messagae = _message

try:
    number = input(" introduce un numero:")
    if (number == "2"):
        raise NoPuedeEscribirDosException("introdujo un numero 2 y este no es valido")

        
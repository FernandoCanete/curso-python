def saludar(name):
    print(f"Hola {name} !!!")

def saludar_dos(first_name, last_name):
    print(f"hola {first_name}, {last_name}!!!")

def multiplicar_texto(texto, multiplier = 2):
    print(texto * multiplier)

def varieltal(param1, param2, *others):
    print(param1)
    print(param2)
    print(others)


def varieltal_dos(param1, **others):
    print(param1)
    print(others)


saludar("Rodrigo")
saludar("Richar")
saludar_dos(last_name ="Lujano", first_name = "Richar")
multiplicar_texto("v", 5)

multiplicar_texto("x")

print("/n-----------/n")
varieltal("1A", "2B", 0, "xx", [0, 1])

print("/n-----------/n")
varieltal_dos("1A", id=0, name = "carlos")





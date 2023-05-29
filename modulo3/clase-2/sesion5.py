

mi_diccionario = {"nombre": "daniel", "edad": 26}
print(mi_diccionario.get("edad"))

empty_dict_2 =dict()
print(empty_dict_2)

full_dict = dict(
    genero = "M" ,
    nacionalidad = "E"
)
print(full_dict)

empleado = {
    "name" : "valeria",
    "apellido" : "roso",
    "edad" : 18,
    "rut": "11.111.111-1"
}

print(empleado)
for variablex in empleado.values():
    print(variablex)

    print(empleado)
    for clave, valor in empleado.items():
        print(clave, valor)

edad = 60
if edad > 50:
    print("Hola Don")
    print("Hola desde adentro de if")

print("aca continua el codigo")


temperatura = 38
if temperatura >= 37:
    print("Alerta de temperatura alta")
else:
    print("La temperatura aun es normal")

    temperatura = 5
    pais = "chile"

    if temperatura < 10:
        if pais == "chile":
            print("cccc")
        else:
            print("zzzz")
    else:
        if pais == "chile":
            print("111")
        else:
            print:("222")


s = 0
if temperatura < 10:
    print("es altamente probable que nieve")
elif temperatura >= 10 and temperatura <= 20:
    print("es medianamiente probable")

want_exit = "n"
while want exit == "n":
    print("hola como estas?")
    want_exit = input("quieres salir S/N")

    print("fuera del while")

    want_exit ="n"
    num_questions = 0
    while want_exit == "n":
        print("hola como estas?")
        want_exit = input("quieres salir s/n?")
        num_questions +- 1
        if num_questions == 3:
            print("alcanzaste el maximo permitido")
            break
        print("se acabo el while")
        
        





volador = "no"
humano = "no"
enmascarado = "no"

if volador == "si":
    if humano == "si":
        if enmascarado == "si":
            print("el superheroe es volador, humano y enmascarado")
        else:
            print("el superheroe es volador, humano, y no usa mascara")
    else:
        if enmascarado =="si":
            print("el personaje es volador, no es humano, y enmascarado")
        else:
            print("el personaje vuela, no es humano y no usa mascara")
else:
    if humano == "si":
        if enmascarado == "si":
            print("el superheroe es volador, humano y enmascarado")
        else:
            print("el superheroe es volador, humano, y no usa mascara")
    else:
        if enmascarado =="si":
            print("el personaje no es volador, humano, y enmascarado")
        else:
            print("el personaje no es volador, no es humano y no usa mascara")        
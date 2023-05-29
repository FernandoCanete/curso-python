requisitos = {
    "titulo" : "requerido",
    "notas" : "requerido" ,
    "foto" : "opcional"
}


print (requisitos)

# acceder a una propiedad
print(f'las notas son de tipo: {requisitos["notas"]}')
print(f'la foto es de tipo: {requisitos["foto"]}')

# modificar una propiedad
requisitos["foto"] = "requerido"
print(f'la foto es de tipo: {requisitos["foto"]}')
requisitos["notas"] = "opcional"
print(f'las notas son de tipo:{requisitos[("notas")]}')

# construir un diccionario de datos para guardar
# la informacion de un avion , coloque al menos 6 propiedades
# imprima tres de ellas y cambie el valor de dos
# al menos debe existir una propiedad boolenada, una entera , una flotante
# un arreglo, un diccionario y un string

mi_diccionario = {
    "vuela" : True ,
    "horas_de vuelo" : 20.5,
    "pilotos" : 2 ,
    "pasajeros" : 200 ,
    "paises que viaja" : ["chile", "venezuela" , "argentina"] ,
    "nombre aerolinea" : "aerochile"
}

# construya un programa que le solicite el peso en kg de una persona
# y si el peso esta entre 60 y 70 recomiende una dieta de 5 comidas altas en carbohidratos
# si el peso esta entre 70 y 80  recomiende una dieta de 4 comidad altas en proteinas
# si el peso es mayor a 80 recomiende una dieta de 3 comidad altas en fibras
# utilice solo diccionarios para agrupar los respectivos menus


comidas = {
    "carbohidratos": ["pan", "arroz", "tallarines", "papas fritas", "pizzas"],
    "proteínas": ["pollo", "vacuno", "pescado", "huevos", "cerdo"],
    "fibras": ["verduras", "frutas", "legumbres"]
}

peso = float(input("ingrese su peso en kilos: "))

if peso >= 60 and peso <= 70:
    print("Le recomendamos una dieta de 5 comidas al día altas en carbohidratos:")
    for comida in comidas["carbohidratos"]:
        print(" " + comida)
elif peso > 70 and peso <= 80:
    print("Le recomendamos una dieta de 4 comidas al día altas en proteínas:")
    for comida in comidas["proteínas"]:
        print(" " + comida)
elif peso > 80:
    print("Le recomendamos una dieta de 3 comidas al día alta en fibras:")
    for comida in comidas["fibras"]:
        print(" " + comida)
else:
    print("su peso no esta considerado para una dieta")




nombres = ['Harry Houdini', 'Newton', 'David Blaine',
           'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']
def hacer_grandioso():
    for i in range(len(nombres)):
        if nombres[i] in ['Harry Houdini', 'David Blaine', 'Teller']:
            nombres[i] = 'El gran ' + nombres[i]
def imprimir_nombres():
    for nombre in nombres:
        print(nombre)
print("Lista completa de nombres:")
imprimir_nombres()
hacer_grandioso()
magos = []
cientificos = []
otros = []

for nombre in nombres:
    if nombre.startswith('El gran'):
        magos.append(nombre)
    elif nombre in ['Newton', 'Hawking', 'Einstein']:
        cientificos.append(nombre)
    else:
        otros.append(nombre)
print("Magos grandiosos:")
for mago in magos:
    print(mago)
print("Científicos:")
for cientifico in cientificos:
    print(cientifico)
print("Otros:")
for otro in otros:
    print(otro)

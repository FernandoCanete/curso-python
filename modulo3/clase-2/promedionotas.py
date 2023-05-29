print("programa promedio puntajes")
print("ingrese primer numero")
puntajeUno = float(input())
print("ingrese segundo numero")
puntajeDos = float(input())
print("ingrese tercer numero")
puntajeTres = float(input())

promedio = (puntajeUno + puntajeDos +puntajeTres)/3
print(promedio)
if promedio <=2:
    print("Nota D")
if promedio >=2.1 and promedio <=5:
    print("Nota C")
if promedio >=5.1 and promedio <=6:
    print("Nota B") 
if promedio >=6.1 and promedio <=7:
    print("Nota A")   
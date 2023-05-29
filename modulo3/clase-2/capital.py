K = float(input("ingrese el capital inicia:"))
Y = float(input("ingrese el interes anual"))
Z = input("ingrese el numero de años")

Y /= 100 # se convierte el porcentaje a deciaml
total = K * (1+Y)** Z

print("el capital final despues de", Z, "años es:",round(total,2))


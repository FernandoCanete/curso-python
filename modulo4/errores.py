while True:
    try:
        edad = int(input("introduce tu edad:"))
        break
    except ValueError:
        print("debes introducir una edad valida")
    except ZeroDivisionError:
        print("la edad debe ser mayor a zero")

dividendo = 100
while True:
    try:
        edad =int(input("introduce tu edad:"))
        calculo = dividendo / edad
        print(f'el resultado es: {calculo}')
    except ValueError:
        print("Debes introducir una edad valida")
    except ZeroDivisionError:
        print("la edad debe ser mayor a zero")
    else:
        print("else se va a ejecutar solo cuando no haya error")
    finally:
        print("finally se va a ejecutar tanto haya un error como no hayaun error")
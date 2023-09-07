# 02 - Determinar el perimetro de un cuadrado

def validateInput():
    while True:
        try: 
            sideAdded = int(input('Ingrese el tamaño del lado del cuadrado: '))
            assert sideAdded > 0 , "El valor ingresado no es valido."
            print("Ingreso exitoso")
            squarePerimeter(sideAdded)
            break       
        except ValueError as error_Value:
            print(error_Value)
        except AssertionError as assertionError:
            print(assertionError)
 
def squarePerimeter(side):
    return print(f'El perimetro del cuadrado ingresado es {side * 4}')

validateInput()
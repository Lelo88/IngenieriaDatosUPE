# 06 - Determinar la hipotenusa de un triangulo rectangulo conocidas las longitudes de sus dos catetos. 
from math import sqrt, pow

def validateInput():
    while True:
        try: 
            number1 = float(input('Ingrese la longitud del cateto opuesto: '))
            number2 = float(input('Ingrese la longitud del cateto adyacente: '))
            assert (number1 > 0 and number2 > 0) , "El valor ingresado es menor a cero. No condice a un lado del triangulo con valor positivo"
            print("Ingreso exitoso")
            sumNumbers(number1, number2)
            break    
        except ValueError as error_Value:
            print(error_Value)
        except AssertionError as assertionError:
            print(assertionError)
    
def sumNumbers(number1, number2):
    return print(f'La hipotenusa de los catetos ingresados es {round(sqrt(pow(number1, 2) + pow(number2, 2)), 2)}')

validateInput()
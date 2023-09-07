# 01 - Determinar el area de un cuadrado

from math import pow

def validateInput():
    while True:
        try: 
            sideAdded = int(input('Ingrese el tamaño del lado del cuadrado: '))
            assert sideAdded > 0 , "El valor ingresado no es valido."
            print("Ingreso exitoso")       
        except ValueError as error_Value:
            print(error_Value)
        except AssertionError as assertionError:
            print(assertionError)
        else: 
            return sideAdded  
        finally:
            print("Intentelo nuevamente")   
    
def squareArea(sideAdded):
    return  print(f'El area del cuadrado ingresado es {int(pow(sideAdded, 2))}')

side = validateInput()
squareArea(side)
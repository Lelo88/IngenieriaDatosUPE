# 09 -  Diseñar un algoritmo que imprima el cuadrado y el cubo de un numero ingresado por teclado

from math import pow

def doubleAndTriple(number):
    return print(f"El cuadrado de {number} es {int(pow(number, 2))} y el cubo de {number} es {int(pow(number, 3))}")
def inputValue():
    while True: 
        try:
            numero = int(input("Ingrese un numero: "))
            assert type(numero) == int, "El valor ingresado no es valido."
            doubleAndTriple(numero)
            break
        except ValueError as error_Value:
            print(error_Value)
        except AssertionError as assertionError:
            print(assertionError)

inputValue()
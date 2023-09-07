# 08 - Crear un algoritmo que muestre por pantalla el doble y el triple de un numero ingresado por teclado

def doubleAndTriple(number):
    return print(f"El doble de {number} es {number * 2} y el triple de {number} es {number * 3}")
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
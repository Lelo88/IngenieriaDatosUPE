# 10 - Diseñar un numero que pida un numero por teclado y luego imprima el numero del siguiente a ingresado

def inputValue():
    while True: 
        try:
            numero = int(input("Ingrese un numero: "))
            assert type(numero) == int, "El valor ingresado no es valido."
            return print(f'El siguiente al numero {numero} es {numero + 1}')
        except ValueError as error_Value:
            print(error_Value)
        except AssertionError as assertionError:
            print(assertionError)

inputValue()
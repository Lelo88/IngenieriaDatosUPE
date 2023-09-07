# 03 - Realiza el algoritmo necesario para crear un programa que sume dos numeros enteros

def validateInput():
    while True:
        try: 
            number1 = int(input('Ingrese el primer numero a sumar: '))
            number2 = int(input('Ingrese el segundo numero a sumar: '))
            print("Ingreso exitoso")
            sumNumbers(number1, number2)
            break    
        except ValueError as error_Value:
            print(error_Value)
        except AssertionError as assertionError:
            print(assertionError)
    
def sumNumbers(number1, number2):
    return print(f'La suma de los números ingresados es {number1 + number2}')

validateInput()
